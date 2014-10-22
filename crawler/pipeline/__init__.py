from crawler.pipeline.deco import beforeafter
from crawler.db.models import Sources
from crawler.db.utils import session_scope
from crawler.parsers import parser_modules
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm.exc import NoResultFound


def before_get_total_records(html):
    return html

def after_get_total_records(result):
    return result

def before_get_links(html):
    return html

def after_get_links(result):
    return result


def before_get_metadata(html):
    return html

def after_get_metadata(result):
    return result

def construct_pipeline(parser_module):
    return {'total_records': beforeafter(before_get_total_records, after_get_total_records)(
        parser_module.get_total_records),
            'links': beforeafter(before_get_links, after_get_links)(
                parser_module.get_links),
            'metadata': beforeafter(before_get_metadata, after_get_metadata)(
                parser_module.get_metadata)}

pipelines = {}

with session_scope() as session:
    for parser_module in parser_modules:
        try:
            name = parser_module.__name__.replace('crawler.parsers.', '')
            source = session.query(Sources).filter(Sources.parser == name).one()
            pipelines[source.id] = construct_pipeline(parser_module)

        except OperationalError:

            print("Error, probably db not initialized. Try python -m crawler.db.setup")

        except NoResultFound:

            print("You db doesn't contain any description of Sources try to add one")






