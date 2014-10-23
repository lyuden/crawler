import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crawler.db.models import Base
from crawler.settings import DB_DESCRIPTOR


engine = create_engine(DB_DESCRIPTOR)

Session = sessionmaker(bind=engine)


def init_db(engine):

    Base.metadata.create_all(engine)

1
if __name__ == "__main__":
    print("Initializing debug db")
    init_db(engine)

    parser = argparse.ArgumentParser()

    parser.add_argument("-s", action="store_true", help="Init test source", default=False)

    args = parser.parse_args()



    if args.s:
        print("Adding test source to db")
        connection = engine.connect()
        connection.execute("INSERT INTO sources VALUES(NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)")
        connection.execute("UPDATE sources SET url_seed='http://localhost:5000/catalog/:PAGINATOR' WHERE rowid=1;")
        connection.execute("UPDATE sources SET page_start='1' WHERE rowid=1;")
        connection.execute("UPDATE sources SET page_offset='0' WHERE rowid=1;")
        connection.execute("UPDATE sources SET items_per_page='7' WHERE rowid=1;")
        connection.execute("UPDATE sources SET parser='example' WHERE rowid=1;")
        connection.close()


