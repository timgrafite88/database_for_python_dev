import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Book, Shop, Publisher, Stock, Sale

# Подключение к базе PostgreSQL
DSN = 'postgresql://postgres:123@localhost:5432/my_music_site'
engine = sqlalchemy.create_engine(DSN)

# Создание объектов
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_shops(publisher_identifier):  # Функция принимает обязательный параметр
    stmt = session.query(
        Book.title, Shop.name, Sale.price, Sale.date_sale
    ).select_from(Shop). \
        join(Stock). \
        join(Book). \
        join(Publisher). \
        join(Sale)

    if publisher_identifier.isdigit():  # Проверяем, является ли строка числом
        results = stmt.filter(Publisher.id == int(publisher_identifier)).all()  # Фильтрация по ID
    else:
        results = stmt.filter(Publisher.name == publisher_identifier).all()  # Фильтрация по имени

    for title, shop_name, price, date_sale in results:  # Проходим по результатам
        print(f"{title: <40} | {shop_name: <10} | {price: <8} | {date_sale.strftime('%d-%m-%Y')}")

if __name__ == '__main__':
    param = input("Введите данные для поиска: ")
    get_shops(param)

session.close()