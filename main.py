import sqlite3

# define connection and cursor
connection = sqlite3.connect('out/data_base.db')
cursor = connection.cursor()

# create tables
table_user = """CREATE TABLE IF NOT EXISTS User (
                                                id INT PRIMARY KEY,
                                                name TEXT,
                                                surname TEXT,
                                                fathers_name TEXT,
                                                email TEXT )"""

table_shop = """CREATE TABLE IF NOT EXISTS Shop (
                                                id INT PRIMARY KEY,
                                                name TEXT,
                                                address TEXT,
                                                post_code INT)"""

table_book = """CREATE TABLE IF NOT EXISTS Book (
                                                id INT PRIMARY KEY,
                                                name TEXT,
                                                author TEXT,
                                                isbn TEXT)"""

table_order = """CREATE TABLE IF NOT EXISTS Order_ (
                                                    id INT PRIMARY KEY,
                                                    reg_date TEXT,
                                                    user_id INT )"""

table_order_item = """CREATE TABLE IF NOT EXISTS OrderItem (
                                                        id INT PRIMARY KEY,
                                                        order_id INT,
                                                        book_id INT ,
                                                        book_quantity INT,
                                                        shop_id INT,
                                                        FOREIGN KEY (order_id) REFERENCES Order_ (id),
                                                        FOREIGN KEY (book_id) REFERENCES Book (id),
                                                        FOREIGN KEY (shop_id) REFERENCES Shop (id))"""
# execute tables
cursor.execute(table_user)
cursor.execute(table_book)
cursor.execute(table_shop)
cursor.execute(table_order)
cursor.execute(table_order_item)

# add values to the tables

user_data = [(1, "Ivan", "Ivanov", "Ivanovich", "ivan@email.com"),
             (2, "Sergey", "Ivanov", "Ivanovich", "sergey@email.com"),
             (3, "Anton", "Ivanov", "Ivanovich", "anton@email.com")]

cursor.executemany("INSERT OR IGNORE INTO User VALUES (?,?,?,?,?)", user_data)

book_data = [(1, "In Search of Lost Time", "Marcel Proust", "88445-7-158-5"),
             (2, "Ulysses", "James Joyce", "88445-7-158-6"),
             (3, "Don Quixote", "Miguel de Cervantes", "88445-7-158-7")]

cursor.executemany("INSERT OR IGNORE INTO Book VALUES (?,?,?,?)", book_data)

shop_data = [(1, "Tony Booker", "Mountain View, California", "88445"),
             (2, "McBookers", "Menlo Park, California", "88446"),
             (3, "BooksForever", "Palo Alto, California", "88447")]

cursor.executemany("INSERT OR IGNORE INTO Shop VALUES (?,?,?,?)", shop_data)

order_data = [(10, "01.10.2021 14:50", 2),
              (20, "01.10.2021 14:55", 3),
              (30, "01.10.2021 14:57", 1)]

cursor.executemany("INSERT OR IGNORE INTO Order_ VALUES (?,?,?)", order_data)

order_item_data = [(1010, 20, 3, 5, 3),
                   (2020, 30, 2, 6, 2),
                   (3030, 10, 1, 8, 1)]

cursor.executemany("INSERT OR IGNORE INTO OrderItem VALUES (?,?,?,?,?)", order_item_data)

connection.commit()

connection.close()

if __name__ == '__main__':
    pass
