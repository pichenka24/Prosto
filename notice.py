import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from ad_realty"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print(row)

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def func(mass1, mass):
    mass1_edit = mass1[3:12]
    mass_edit = mass[3:12]
    id = mass[1]
    if mass1_edit[0] in mass_edit[0]:
        print('cool')





mass1 = [4, None, 'tenant', 'Кондо', '2 и более', '2 и более', 23, 'Частный и Общественный', 'Нет', 'Есть', '5 дней', 5000, None, 'коммент', '<a href="https://t.me/coolprich">Егор</a>', None, '2023-08-29']
mass = [3, 587386190, 'landlord', 'Кондо', 1, 1, 28, 'Общественный', 'Есть', 'Можно', '1 месяц', '9500 Бат в мес, 7500 Бат\xa0 при долгосрочной аренде\xa0от 4х месяцев.', '1 мин езды от Blue Port', 'Сдам кондо в My Style Condo Huahin. 102 Soi. Бассейн,джакузи,тренажёрный зал на территории.', '<a href="https://t.me/MarinaR369">Marina</a>', 'static/photos/AgACAgIAAxkBAAJvkmTGSrcVX7mGhutNA_EZRszcaPFYAAKpyzEbAsowSoZXS7ryCmrpAQADAgADbQADLwQ.jpg', '2023-08-29']

func(mass1, mass)