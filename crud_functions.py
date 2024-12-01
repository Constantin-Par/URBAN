import sqlite3

def initiate_db():
    def insert_product(title, description, price, image_path):
        with open(image_path, 'rb') as file: img = file.read()
        cursor.execute('INSERT INTO Products (title, description, price, image_path) VALUES (?, ?, ?, ?)',
                       (title, description, price, image_path))

    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
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
    connection.commit()
    connection.close()



def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    return products
    connection.commit()
    connection.close()

if __name__ == '__main__':
    initiate_db()