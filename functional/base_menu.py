import sqlite3

def createTableMenu():
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS menumak (
                                    id INTEGER PRIMARY KEY,
                                    dish TEXT NOT NULL,
                                    structure TEXT NOT NULL
                                );'''
        cursor.execute(create_table_query)
        sqlite_connection.commit()
        print("Таблица создана успешно.")
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")
            
def insertManyData(records):
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        insert_data_query = '''INSERT INTO menumak (id, dish, structure)
                               VALUES (?, ?, ?);'''
        cursor.executemany(insert_data_query, records)
        sqlite_connection.commit()
        print("Записей успешно добавлено:", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")
            
def selectTable():
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")
        print()

        sqlite_select_query = "SELECT * FROM menumak;"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При работе с базой данных возникла ошибка:", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто.")
            
menumak = [("1", "Humburger", "Bun, beef, tomatoes, cheese"),
           ("2", "Crisps", "Potato, salt"),
           ("3", "Ice cream", "Milk, chocolate, caramel, nuts"),
           ("4", "Nuggets", "Hen"),
           ("5", "Pita", "Dough, chicken, tomatoes, cucumbers"),]
            
# createTableMenu()
# insertManyData(menumak)