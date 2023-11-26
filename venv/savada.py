import sqlite3
from sqlite3 import Error


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except Error:
        print(Error)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_product(conn, product: tuple):
    try:
        sql = '''INSERT INTO products
        (product_title, price, quantity)
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def create_products(conn):
    create_product(conn, ('Кефир', 17.80, 7))  # 1
    create_product(conn, ('Мороженое: Бахрома', 60.53, 30))  # 2
    create_product(conn, ('Пепси 2л', 135.00, 4))  # 3
    create_product(conn, ('NITRO', 62.40, 12))  # 4
    create_product(conn, ('Контик', 34.90, 5))  # 5
    create_product(conn, ('Жидкое мыло', 67.89, 2))  # 6
    create_product(conn, ('Мыло детское', 108.60, 7))  # 7
    create_product(conn, ('Кириешки Flint', 26.12, 20))  # 8
    create_product(conn, ('Семечки Джин', 59.99, 6))  # 9
    create_product(conn, ('Гамбургер "Тойбосс"', 105.00, 3))  # 10
    create_product(conn, ('Alpen Gold', 114.59, 4))  # 11
    create_product(conn, ('Asu!', 33.40, 8))  # 12
    create_product(conn, ('Моющее средство', 73.70, 4))  # 13
    create_product(conn, ('Порошок', 250.00, 3))  # 14
    create_product(conn, ('Подсолнечное Масло', 240.00, 5))  # 15
    create_product(conn, ('Сливочное Масло', 340.00, 7))  # 16
    create_product(conn, ('Масло для бутербротов', 300.00, 15))  # 17
    create_product(conn, ('Домашнее Масло', 150.00, 5))  # 18
    create_product(conn, ('Заводское Масло', 200.00, 12))  # 19
    create_product(conn, ('Детское-лечебное Масло', 400.00, 2))  # 20



def update_product_quantity(conn, product: tuple):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def update_product_price(conn, product: tuple):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except Error:
        print(Error)


def delete_product_by_id(conn, id: int):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def print_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def print_all_products_by_price_and_quntity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100.0 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def search_by_word(conn, word):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))

        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


connection = create_connection("hw.db")

create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR (200) NOT NULL,
price DOUBLE (10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (5) NOT NULL DEFAULT 0
)
'''

if connection is not None:
    print('Connected Successfully!')
    create_products(connection)
    create_table(connection, create_products_table)
    print_all_products_by_price_and_quntity(connection)
    search_by_word(connection, 'мыло' or 'Масло')
    print('Done')
