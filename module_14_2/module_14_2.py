import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS Users')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''')
for id_user in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{id_user}', f'example{id_user}@gmail.com', id_user * 10, 1000))
cursor.execute('UPDATE Users SET balance = ? WHERE (id+1) %2 = 0', (500,))
cursor.execute('DELETE FROM Users WHERE (id+2) % 3 = 0')
cursor.execute('SELECT * FROM Users WHERE age <> ?', (60,))
users = cursor.fetchall()
print('\n'.join([f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}' for user in users]))

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Количество Users: {total_users}')

cursor.execute('SELECT SUM(balance) FROM Users')
all_balanses = cursor.fetchone()[0]
print(f'Сумма балансов: {all_balanses}')

print(f'Средний баланс: {all_balanses/total_users}')

connection.commit()
connection.close()
