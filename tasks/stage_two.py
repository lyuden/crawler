# Processing depth 0 url

from settings import app
from db.utils import session_scope
from db.models import Urls,Sources
from tasks.utils import add_paginated_url
from parsers import parser_functions, limit_finder
import datetime
import requests

@app.task(name='get_html')
def get_html(url_id):

    with session_scope() as session:
        url = session.query(Urls).filter(Urls.id == url_id).one()
        url.visited_at = datetime.datetime.now()
        session.add(url)
        r = requests.get(Urls.url)

    return r.contents




@app.task(name='generate_depth_zero_tasks')
def generate_depth_one_processing_tasks():

    with session_scope() as session:

        for url in session.query(Urls).filter(Urls.depth == 0).all():
            # We don't need source id in get_html function but need it in process_subtask hence we are using partial
            process_subtask = process_depth_one.s(url.source_id)
            get_html.apply_async((url.id,), link=process_depth_one)



@app.taks(name='process_depth_one_task')
def process_depth_one(html,source_id):

    limit = limit_finder(html)

    with session_scope() as session:
        source = session.query(Sources).filter(Sources.id == source_id).one()

        for i in range(source.page_start +1, limit +1 ):
            add_paginated_url(session,page=i,template=source.url_seed,source_id=source.id)


    extract_products_urls.apply_async((html,source_id))

@app.task(name="extract_product_urls_task")
def extract_products_urls(html,source_id):

    for product_url in parser_functions[source_id]:

        get_html((product_url,), link = parse_product)

@app.task
def parse_product(html):








