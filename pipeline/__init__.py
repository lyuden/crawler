from pipeline.deco import beforeafter
from db.models import Sources
from db.utils import session_scope
from parsers import parser_modules
import re


def construct_pipeline(parser_module):
    return {'total_records': beforeafter(parser_module.before_get_total, parser_module.before_get_total)(
        parser_module.get_total),
            'links': beforeafter(parser_module.before_get_links, parser_module.after_get_links)(
                parser_module.get_links),
            'metadata': beforeafter(parser_module.before_get_metadata, parser_module.after_get_metadata)(
                parser_module.get_metadata)}

pipelines = {}

with session_scope() as session:
    for parser_module in parser_modules:
        name = parser_module.__name__.replace('parsers.', '')
        source = session.query(Sources).filter(Sources.parser == name)
        pipelines[source.id] = construct_pipeline(parser_module)





