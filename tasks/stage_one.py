from db.utils import session_scope
from db.models import Sources
from tasks.utils import add_paginated_url
from settings import app





@app.task(name="form_depth_zero_urls_task")
def form_depth_zero_urls():
    with session_scope() as session:
        for source in session.query(Sources).all():
            add_paginated_url(session, source.url_seed, source.page_start, source.id)





