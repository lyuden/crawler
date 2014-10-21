import re
from _datetime import datetime

from crawler.db.models import Urls
from crawler.settings import PAGINATOR_REGEXP


def add_paginated_url(session, template, page, source_id, logger=None):
    url_string = re.sub(PAGINATOR_REGEXP, str(page), template)
    print(url_string, page)
    try:
        url = session.query(Urls).filter(Urls.url == url_string).one()
        url.active_at = datetime.now()
        if logger:
            logger.debug('Found {} in database with id = {}. Do nothing'.format(url_string, url.id))
    except:
        url = Urls(source_id=source_id, url=url_string, depth=0, alive_at=datetime.now())
        session.add(url)


