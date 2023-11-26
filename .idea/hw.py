import sqlite3


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def create_table(conn, sql):
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute(sql, product)
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows_list = cursor.fetchall()

        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

#  ВЫВОД В КОНСОЛЬ ВСЕ ПРОДУКТЫ ИЗ ТАБЛИЦЫ 'products'
def select_products_by_price(conn, price_limit):
    sql = '''SELECT * FROM products WHERE price < ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(price_limit))
        row_list = cursor.fetchall()

        for row in row_list:
            print(row)
    except sqlite3.Error as e:
        print(e)

# ОБНОВЛЕНИЕ КОЛИЧЕСТВО ПРОДУКТОВ В 'quantity'
def update_product_quantity(conn, product):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

# УДАЛЕНИЕ ЗАПИСИ В ТАБЛИЦЕ 'products'
def delete_product(conn, product_id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (product_id))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

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

sql_to_create_products_table = '''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER(5) NOT NULL DEFAULT 0 
)
'''

connection = create_connection('hw.db')
if connection is not None:
    print('Успешно подключено к базе данных!')
    create_table(connection, sql_to_create_products_table)

    insert_product(connection,('Мыло', 50, 20))
    insert_product(connection,('Жидкое мыло', 80, 24))
    insert_product(connection,('Бумага', 20, 100))
    insert_product(connection,('Салфетки', 10, 80))
    insert_product(connection,('Влажные солфетки', 23, 73))
    insert_product(connection,('Шампунь', 120, 35))
    insert_product(connection,('Тетрадь', 5, 120))
    insert_product(connection,('Ручка', 10, 45))
    insert_product(connection,('Маркер', 20, 20))
    insert_product(connection,('Фломастер', 80, 68))
    insert_product(connection,('Ластик', 3, 31))
    insert_product(connection,('Султан Чай', 50, 24))
    insert_product(connection,('Кола', 80, 42))
    insert_product(connection,('Шоколад', 45, 88))
    insert_product(connection,('Кофе', 15, 25))
    select_all_products(connection)
    select_products_by_price(connection,20.0)
    update_product_quantity(connection,(80, 1))
    delete_product(connection, 5)
    search_by_word(connection, 'мыло' or 'Масло')


    connection.close()