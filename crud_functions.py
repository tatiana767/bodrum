import sqlite3


connection = sqlite3.connect("db_module_14_3.db")
cursor  = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY , 
    title TEXT NOT NULL, 
    description TEXT NOT NULL, 
    price INTEGER NOT NULL )
    ''')

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS Users(
      id INTEGER PRIMARY KEY , 
      name TEXT NOT NULL, 
      email TEXT NOT NULL,
      age INTEGER NOT NULL, 
      balance INTEGER NOT NULL
       )
      ''')

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users(name, email, age, balance ) values(?, ?, ?, ?)",
                   (f"{username}", f"{email}", f"{age}", f"{1000}"))

def is_included(username):
   user = cursor.execute(f"SELECT count(name) FROM Users where Users.name == '{username}'").fetchone()
   if user[0] > 0 :
        return True
   else:
        return False

def fill_db():
    description = ['Витамины для красоты', 'Витамины для сосудов', 'Витамины для сердца', 'Витамины для памяти']
    for i in range(0,4):
        cursor.execute("INSERT INTO Products( title, description, price ) values(?, ?, ?)", (f"Продукт{i+1}", f"{description[i]}", f"{1000*i + 354}"))


def get_all_products():
    cursor.execute("Select * from Products")
    products = cursor.fetchall()
    return products


connection.commit()


initiate_db()
fill_db()
print(get_all_products()[0][0])

def close_connection():
    connection.close()