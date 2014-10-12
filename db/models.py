from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Products(Base):
    id = Column(String(32), default='')
    source_id = Column(Integer)
    url = Column(Text)
    title = Column(String(90))
    description = Column(Text)
    created_at = Column(DateTime)

class Sources(Base):
    __tablename__ = 'sources'
    id = Column(Integer, primary_key=True)
    url_seed = Column(Text)
    page_start = Column(Integer, default=None)
    page_offset = Column(Integer, default=None)
    items_per_page = Column(Integer, default=None)
    parser = Column (String(32), default=None)
    encoding = Column (String(10), default='utf-8')
    country = Column(String(3), default=None)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)
    status = Column(Integer, default=0 )

class Urls(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, default=None)
    url = Column(Text)
    depth = Column(Integer)
    alive_at = Column(Integer, default=None)
    visited_at = Column(Integer, default=None)
    crated_at = Column(Integer, default=None)
