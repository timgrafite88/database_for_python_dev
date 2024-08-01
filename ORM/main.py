import sqlalchemy
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Shop, Publisher, Stock, Sale

# подключение к базе PostgreSQL
DSN = 'postgresql://postgres:123@localhost:5432/my_music_site'

engine = sqlalchemy.create_engine(DSN)

# #создание объектов
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publ = input('Введите Фамилию писателя: ')

subq = session.query(Publisher).filter(Publisher.name == publ).all()

stmnt = (
    select(
        #Book.title,Shop.name, Sale.price, Sale.date_sale
        Sale
        )
#    .select(Shop)
    .join(Stock, Sale.id_stock == Stock.id)
    .join(Shop, Stock.id_shop == Shop.id)
    .join(Book, Book.id == Stock.id_book)
    .join(Publisher, Publisher.id == Book.id_publisher)
    .where(Publisher.name == publ)
)

for i in session.scalars(stmnt):
    print(i)

session.close()