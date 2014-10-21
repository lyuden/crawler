# Processing depth 0 url

from _datetime import datetime

from sqlalchemy.orm.exc import NoResultFound
import requests
from celery.utils.log import get_task_logger

from crawler.celeryapp import app
from crawler.db.utils import session_scope
from crawler.db.models import Urls, Sources, Products
from crawler.tasks.utils import add_paginated_url
from crawler.pipeline import pipelines


logger = get_task_logger(__name__)

@app.task(name='get_html')
def get_html(url_string):



    logger.debug("Trying to get html from {}".format(url_string))
    with session_scope() as session:
        try:
            url = session.query(Urls).filter(Urls.url == url_string).one()
            logger.debug("Found {} in Urls with id = {} ".format(url_string, url.id))
        except NoResultFound:
            logger.debug("Couldn't find {} in Urls table returning empty string".format(url_string))
            return ''

        url.visited_at = datetime.now()
        session.add(url)
    logger.debug("Performing network request")
    r = requests.get(url_string)
    logger.debug("Network request is ok {}".format(r.ok))

    return r.content


@app.task(name='generate_depth_zero_tasks')
def generate_depth_one_processing_tasks():

    print("Hello")
    logger.debug("Generating depth = 1 urls and tasks")
    with session_scope() as session:
        for url in session.query(Urls).filter(Urls.depth == 0).all():
            print(url.url)
            # We don't need source id in get_html function but need it in process_subtask hence we are using partial. Look celery documentation
            process_subtask = process_depth_one.s(url.source_id)
            get_html.apply_async((url.url,), link=process_subtask)


@app.task(name='process_depth_one_task')
def process_depth_one(html, source_id):
    limit = pipelines[source_id]['total_records'](html)

    logger.debug('Found limit of {}'.format(limit))
    with session_scope() as session:
        source = session.query(Sources).filter(Sources.id == source_id).one()

        for i in range(source.page_start + 1, limit + 1):
            add_paginated_url(session, page=i, template=source.url_seed, source_id=source.id)

    extract_products_urls.apply_async((html, source_id))


@app.task(name="extract_product_urls_task")
def extract_products_urls(html, source_id):
    for product_url in pipelines[source_id]['links'](html):

        with session_scope() as session:

            try:
                product_url_object = session.query(Urls).filter(Urls.url == product_url).one()

            except NoResultFound:

                product_url_object = Urls(source_id=source_id,
                                          url=product_url,
                                          depth=2,
                                          alive_at=datetime.now(),
                                          )

                session.add(product_url_object)

        extract_metadata_subtask = parse_product.s(product_url, source_id)

        get_html.apply_async((product_url,), link=extract_metadata_subtask)


@app.task(name='parse_product_task')
def parse_product(html, product_url, source_id):
    with session_scope() as session:
        product_dict = pipelines[source_id]['metadata'](html)
        product_dict.update({

            'url': product_url,
            'source_id': source_id

        })
        product = Products(**product_dict)
        session.add(product)








