from celery.utils.log import get_task_logger

from crawler.db.utils import session_scope
from crawler.db.models import Sources
from crawler.tasks.utils import add_paginated_url
from crawler.celeryapp import app


logger = get_task_logger(__name__)

@app.task(name="form_depth_zero_urls_task")
def form_depth_zero_urls():

    with session_scope() as session:
        for source in session.query(Sources).all():
            print(source.page_start)
            add_paginated_url(session, source.url_seed, source.page_start, source.id, logger=logger)





