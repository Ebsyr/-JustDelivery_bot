import sqlite3

def createTableMenu():
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS restaurant (
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

        insert_data_query = '''INSERT INTO restaurant (id, dish, structure)
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

        sqlite_select_query = "SELECT * FROM restaurant;"
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
            
menu = [("1", "Omlette", "Two eggs"),
        ("2", "Salad", "Tomatoes, cucumbers, sour cream"),
        ("3", "Roast meat", "Meat, greenery"),
        ("4", "Puree", "Potatoes"),
        ("5", "Baked chicken", "Chicken")]

# createTableMenu()
# insertManyData(menu)
# print(selectTable())