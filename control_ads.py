import datetime as DT
import sqlite3
import time


def control_transport(current_date):

    try:
        sqlite_connection = sqlite3.connect('db.db')
        cursor = sqlite_connection.cursor()
        forma = f"DELETE FROM ad_transport WHERE last_date = date('{current_date}'); "

        cursor.execute(forma)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite2", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def control_realty(current_date):
    try:
        sqlite_connection = sqlite3.connect('db.db')
        cursor = sqlite_connection.cursor()
        forma = f"DELETE FROM ad_realty WHERE last_date = date('{current_date}'); "

        cursor.execute(forma)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite2", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


while True:
    control_transport(DT.datetime.now().date())
    control_realty(DT.datetime.now().date())
    time.sleep(86400)

