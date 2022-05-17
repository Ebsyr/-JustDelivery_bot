import sqlite3


def createTableOrder():
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        create_table_query = '''CREATE TABLE IF NOT EXISTS doorder (
                                    id TEXT NOT NULL,
                                    address TEXT NOT NULL,
                                    name TEXT NOT NULL,
                                    phone TEXT NOT NULL,
                                    wishes TEXT NOT NULL
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

        insert_data_query = '''INSERT INTO doorder (id, address, name, phone, wishes)
                               VALUES (?, ?, ?, ?, ?);'''
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
            
def insertManyDataMode(id, address, name, phone, wishes):
    try:
        sqlite_connection = sqlite3.connect("delivery.db")
        cursor = sqlite_connection.cursor()
        print("База данных создана и подключена к SQLite.")

        insert_data_query = '''INSERT INTO doorder (id, address, name, phone, wishes)
                               VALUES (?, ?, ?, ?, ?);'''
        cursor.execute(insert_data_query, (id, address, name, phone, wishes))
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

        sqlite_select_query = "SELECT * FROM doorder;"
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
            
# createTableOrder()
