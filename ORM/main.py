import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Shop, Publisher, Stock, Sale


DSN = 'postgresql://postgres:123@localhost:5432/my_music_site'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()