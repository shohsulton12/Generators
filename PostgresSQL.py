import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            dbname="n42",
            user="postgres",
            password="123",
            host="localhost",
            port="5432",
            options="-c search_path=dbo,sql"
        )
        return conn
    except psycopg2.Error as e:
        print("Error in sign in to sql", e)
        return None

def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        create table if not exists Product (
            id serial primary key,
            name varchar(255),
            price   int not null
        )
    """)
    conn.commit()
    print("Produc table created successfully")
    cur.close()
    conn.close()

def insert(name, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        insert into Product (name, price)
        values (%s, %s)
    """, (name, price))
    conn.commit()
    print("Datas inserted successfully")
    cur.close()
    conn.close()

def select_all():
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from Product")
    rows = cur.fetchall()
    print("List of products found successfully:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def select_one(product_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("select * from Product where id = %s", (product_id,))
    row = cur.fetchone()
    if row:
        print("ID", product_id, ":", row)
    else:
        print("ID", product_id, "NOT FOUND")
    cur.close()
    conn.close()

def update(product_id, new_name, new_price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        update Product
        set name = %s, price = %s
        where id = %s
    """, (new_name, new_price, product_id))
    conn.commit()
    print("Updated product successfully")
    cur.close()
    conn.close()

def delete(product_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from Product where id = %s", (product_id,))
    conn.commit()
    print("Delete data successfully")
    cur.close()
    conn.close()

create_table()

insert("Phone", 500)
insert("lap top", 1200)

select_all()

select_one(1)

update(1, "Watch", 600)

select_one(1)

delete(2)
