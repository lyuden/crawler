from db.models import Base
from sqlalchemy import create_engine
from settings import DB_DESCRIPTOR
from sqlalchemy.orm import sessionmaker

engine = create_engine(DB_DESCRIPTOR)

Session = sessionmaker(bind=engine)


def init_db(engine):

    Base.metadata.create_all(engine)
