from pipeline.deco import beforeafter
from db.models import Sources
from db.utils import session_scope
from parsers import parser_modules
import re


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
        parser_module.get_total),
            'links': beforeafter(before_get_links, after_get_links)(
                parser_module.get_links),
            'metadata': beforeafter(before_get_metadata, after_get_metadata)(
                parser_module.get_metadata)}

pipelines = {}

with session_scope() as session:
    for parser_module in parser_modules:
        name = parser_module.__name__.replace('parsers.', '')
        source = session.query(Sources).filter(Sources.parser == name)
        pipelines[source.id] = construct_pipeline(parser_module)





