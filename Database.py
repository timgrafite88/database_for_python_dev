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
                
                create table phones (phone_number int,
                   client_id int references clients(client_id));""")

    conn.commit()


def add_client(conn, first_name, last_name, email, phones=None):
    """Функция добавления клиента"""
    cur = conn.cursor()

    cur.execute(f"""
    insert into clients (first_name, last_name, email) 
    values ({first_name}, {last_name}, {email}); 
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
    pass

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
    pass

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    pass


with psycopg2.connect(host = 'localhost', database="postgres", user="postgres", password="123") as conn:
    #create_db(conn)


conn.close()