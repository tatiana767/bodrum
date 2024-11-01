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



connection.commit()

cursor.execute("Select * from Users where Users.age != 60")
users = cursor.fetchall()
print("fuck")
for user in users :
    print(user)

connection.close()

'''Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
'''