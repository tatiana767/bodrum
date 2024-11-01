'''Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователей.'''

import sqlite3
connection = sqlite3.connect("not_telegram.db")
cursor  = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY , 
user_name TEXT NOT NULL, 
email TEXT NOT NULL, 
age INTEGER,
balance INTEGER NOT NULL)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON USERS(email)")

for i in range(1, 11):
     cursor.execute("INSERT INTO Users(user_name, email, age, balance) VALUES (?, ?, ?, ?) ", (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))




for i in range(1, 11, 2):
   cursor.execute("UPDATE Users set balance = ? where id = ?",("500", f"{i}"))



for i in range(1, 11, 3):
        cursor.execute("DELETE  from Users  where id = ?", (f"{i}",))


cursor.execute("DELETE  from Users  where id == 6 ")
connection.commit()

cursor.execute("Select * from Users where Users.age != 60")
cursor.execute("Select count(*) from Users")
count = cursor.fetchone()[0]
cursor.execute("Select SUM(balance) from Users")
balance = cursor.fetchone()[0]

print("count = ", count)
print("balane = ", balance)
print("AVG = ", balance / count)

cursor.execute("Select AVG(balance) from Users")
avg_balance = cursor.fetchone()[0]
print("avg_balane = ", avg_balance)


connection.close()
