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

def add_client(conn, first_name, last_name, email, phones=None):
    """Функция добавления клиента"""
    cur = conn.cursor()

    cur.execute("""
    insert into clients (first_name, last_name, email) 
    values (%s, %s, %s); 
                """, (first_name, last_name, email))

    #добавляем телефон, если он указан
    if phones is not None:
        cur.execute("""
        insert into phones (client_id, phone_number)
        values ((select client_id 
                from clients 
                where first_name = %s
                    and last_name = %s
                    and email = %s), %s);
        """, (first_name, last_name, email, phones))


def add_phone(conn, client_id, phone):
    """Функция добавления телефона"""
    cur = conn.cursor()
    cur.execute(f"""
                insert into phones (client_id, phone)
                values (%s, %s);
                """, (client_id, phone))

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    """Функция изменения данных клиента"""
    cur = conn.cursor()

    #если в функцию подаем номер телефона, то заменяем его
    if phones is not None:
        cur.execute("""
        update phones
        set phone_number = %s
        where client_id = %s;
        """, (phones, client_id)
        )

    if first_name is not None:
        cur.execute("""
        update clients
        set first_name = %s
        where client_id = %s;
        """, (first_name, client_id)
        )

    if last_name is not None:
        cur.execute("""
        update clients
        set last_name = %s
        where client_id = %s;
        """, (last_name, client_id)
        )

    if email is not None:
        cur.execute("""
            update clients
            set email = %s
            where client_id = %s;
            """, (email, client_id)
                )



def delete_phone(conn, client_id, phone):
    """Функция удаления телефона"""
    cur = conn.cursor()
    cur.execute("""
                    delete from phones
                    where client_id = %s
                        and phone = %s;
                    """, (client_id, phone))


def delete_client(conn, client_id):
    """Функция удаления информации о клиенте"""
    cur = conn.cursor()
    cur.execute("""
                        delete from phones
                        where client_id = %s;
                        
                        delete from clients
                        where client_id = %s;
                        """, (client_id, ))


def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    """Функция поиска клиента по данным"""
    cur = conn.cursor()

    if phone is not None:
        cur.execute("""select first_name, last_name, email, phone_number
                                from clients c
                                    join phones p on c.client_id = p.client_id
                                where p.phone_number = %s
                                ;""", (phone,))

    else:
        cur.execute("""select first_name, last_name, email, phone_number
                        from clients c
                            join phones p on c.client_id = p.client_id
                        where c.first_name = %s
                            or c.last_name = %s
                            or c.email = %s
                        ;""", (first_name, last_name, email))

    for row in cur.fetchall():
        print(row)


if __name__ == "__main__":
    with psycopg2.connect(host = 'localhost', database="postgres", user="postgres", password="123") as conn:
        change_client(conn,client_id=2, phones=777777)

    conn.close()