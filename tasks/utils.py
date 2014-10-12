from db.models import Urls
from settings import PAGINATOR_REGEXP

def add_paginated_url(session, template, page, source_id):
    url_string = re.sub(PAGINATOR_REGEXP,str(page),template)
    url = Urls(source_id=source_id, url=url_string, depth=0)
    # TODO check duplicate URLS ( Think about ditching string field altogether and putting just page number and source_id instead)
    session.add(url)
