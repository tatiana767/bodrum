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


#connection.close()