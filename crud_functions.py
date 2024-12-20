import sqlite3

connection = sqlite3.connect('telega.db')
cursor = connection.cursor()

def initiate_db():
    def insert_product(title, description, price, image_path):
        with open(image_path, 'rb') as file: img = file.read()
        cursor.execute('INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)',
                       (title, description, price, image_path))

    cursor.execute('DROP TABLE IF EXISTS Products')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER,
    image_path TEXT)
    ''')
    insert_product('Вело 1', 'Желтый байк', 56000, 'p1.jpg')
    insert_product('Вело 2', 'Синий байк', 61000, 'p2.jpg')
    insert_product('Вело 3', 'Черный байк', 52000, 'p3.jpg')
    insert_product('Вело 4', 'Зелено-оранжевый байк', 99000, 'p4.jpg')
    insert_product('Вело 5', 'WOW', 999000, 'p5.jpg')

    cursor.execute('DROP TABLE IF EXISTS Users')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL)
    ''')
    add_user('Georg', 'georg@gmail.com', 23)
    add_user('Katy', 'katy@gmail.com', 28)
    add_user('Tom', 'tom@gmail.com', 31)
    add_user('Greg', 'greg@gmail.com', 45)
    add_user('Anthony', 'anthony@gmail.com', 19)
    add_user('Mary', 'mary@gmail.com', 25)

    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products

def add_user(username, email, age):
    if is_included(username):
        return
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))
    connection.commit()

def is_included(username):
    user = cursor.execute('SELECT * FROM Users WHERE username=?', (username, )).fetchone()
    return user is not None

if __name__ == '__main__':
    initiate_db()
    connection.close()