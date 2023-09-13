import sqlite3


def read_sqlite_table():
    try:
        conn = sqlite3.connect('db.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ad_realty ")

        rows = cur.fetchall()

        ads = []
        for row in rows:
            ads.append(list(row))

        print(ads)

        cur.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Соединение с SQLite закрыто")


read_sqlite_table()
