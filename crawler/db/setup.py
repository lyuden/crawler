from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crawler.db.models import Base
from crawler.settings import DB_DESCRIPTOR


engine = create_engine(DB_DESCRIPTOR)

Session = sessionmaker(bind=engine)


def init_db(engine):

    Base.metadata.create_all(engine)
