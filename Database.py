import psycopg2

def create_db(conn):
    """Функция создания таблиц"""
    cur = conn.cursor()
    cur.execute("""
                drop table if exists clients;
                
                drop table if exists phones;
                
                create table clients (client_id serial primary key, first_name varchar(100) not null,
                last_name varchar(100) not null,
                email varchar(50) not null);
                
                create table phones (phone_number int check(len(phone_number) = 10),
                   client_id int references clients(client_id));""")

    conn.commit()


def add_client(conn, first_name, last_name, email, phones=None):
    """Функция добавления клиента"""
    cur = conn.cursor()

    cur.execute(f"""
    insert into clients (first_name, last_name, email) 
    values ('{first_name}', '{last_name}', '{email}'); 
                """)
    conn.commit()

    #добавляем телефон, если он указан
    if phones is not None:
        cur.execute(f"""
        insert into phones (client_id, phone_number)
        values ((select client_id 
                from clients 
                where first_name = '{first_name}'
                    and last_name = '{last_name}'
                    and email = '{email}'), {phones});
        """)
    conn.commit()


def add_phone(conn, client_id, phone):
    """Функция добавления телефона"""
    cur = conn.cursor()
    cur.execute(f"""
                insert into phones (client_id, phone)
                values ({client_id}, {phone});
                """)
    conn.commit()

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    """Функция изменения данных клиента"""
    cur = conn.cursor()

    if phones is not None:
        cur.execute(f"""update phones set phone_number = {phones} where client_id = {client_id};""")

    if first_name is not None:
        cur.execute(f"""update clients set first_name = {first_name} where client_id = {client_id};""")

    if last_name is not None:
        cur.execute(f"""update clients set last_name = {last_name} where client_id = {client_id};""")

    if email is not None:
        cur.execute(f"""update clients set email = {email} where client_id = {client_id};""")

    conn.commit()


def delete_phone(conn, client_id, phone):
    """Функция удаления телефона"""
    cur = conn.cursor()
    cur.execute(f"""
                    delete from phones
                    where client_id = {client_id}
                        and phone = {phone};
                    """)
    conn.commit()


def delete_client(conn, client_id):
    """Функция удаления информации о клиенте"""
    cur = conn.cursor()
    cur.execute(f"""
                        delete from phones
                        where client_id = {client_id};
                        
                        delete from clients
                        where client_id = {client_id};
                        """)
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    """Функция поиска клиента по данным"""
    cur = conn.cursor()

    if phone is not None:
        cur.execute(f"""select first_name, last_name, email, phone_number
                                from clients c
                                    join phones p on c.client_id = p.client_id
                                where p.phone_number = {phone}
                                ;""")

    else:
        cur.execute(f"""select first_name, last_name, email, phone_number
                        from clients c
                            join phones p on c.client_id = p.client_id
                        where c.first_name = '{first_name}'
                            or c.last_name = '{last_name}'
                            or c.email = '{email}'
                        ;""")

    for row in cur.fetchall():
        print(row)


with psycopg2.connect(host = 'localhost', database="postgres", user="postgres", password="123") as conn:
    create_db(conn)

conn.close()