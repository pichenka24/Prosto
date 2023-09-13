# from telethon import TelegramClient
# import time
# import sqlite3
#
# from config import api_id, api_hash
# from questions import repeat_msg_1, repeat_msg_0
#
# client = TelegramClient('anon', api_id, api_hash)
#
#
# async def send_msg(name, msg):
#     await client.send_message(f'{name}', f'{msg}', parse_mode='HTML')
#
#
# def methods(names, msg):
#     print(names, msg)
#     with client:
#         for name in names:
#             client.loop.run_in_executor(send_msg(name, msg))
#             time.sleep(1)
#
#
# def get_ads(person=1):
#     try:
#         sqlite_connection = sqlite3.connect('db.db')
#         cursor = sqlite_connection.cursor()
#         if person == 0:
#             forma = f"SELECT * from ad_realty WHERE person='landlord'"
#         if person == 1:
#             forma = f"SELECT * from ad_transport WHERE category='landlord'"
#
#         cursor.execute(forma)
#         records = cursor.fetchall()
#
#         mass = []
#         for el in records:
#             element = list(el)
#             mass.append(element)
#         cursor.close()
#         return mass
#     except Exception as _ex:
#         print(_ex)
#
#
# def remake_ad(ad, username, category):
#     # ad.append(username)
#     if category == 0:
#         if len(ad[1]) > 1:
#             ad[1] = int(ad[1].split()[0])
#         elif type(ad[1]) == str:
#             ad[1] = int(ad[1])
#
#         if len(ad[2]) > 1:
#             ad[2] = int(ad[2].split()[0])
#         elif type(ad[2]) == str:
#             ad[2] = int(ad[2])
#         ad[3] = int(ad[3])
#         ad[8] = int(ad[8])
#     elif category == 1:
#         ad[4] = int(ad[4])
#     return ad
#
#
# def remake_ads(ads, category):
#     sat_ads = []
#     if category == 0:
#         for i in ads:
#             mass = i
#             mass = mass[2:]
#             mass.pop(12)
#             # print(f'com -> {mass}')
#             if type(mass[1]) == str:
#                 mass[1] = int(mass[1].split()[0])
#             elif type(mass[2]) == str:
#                 mass[2] = int(mass[2].split()[0])
#
#             mass[8] = int(mass[8])
#             sat_ads.append(mass)
#     elif category == 1:
#         for i in ads:
#             mass = i
#             mass = mass[2:]
#             mass.pop(7)
#             sat_ads.append(mass)
#     return sat_ads
#
#
# def create_msg(ads, ad, category):
#     access_landlords = []
#     msg = ''
#     if category == 0:
#         for i in ads:
#             if ad[0] in i and ad[1] <= i[1] and ad[2] <= i[2] and ad[3] <= i[3] and ad[8] >= i[8]:
#                 access_landlords.append(i[11].split('"')[1])
#         for sent in range(len(ad)-1):
#             msg += f'<b>{repeat_msg_0[1][sent][0]}</b> ' + str(ad[sent]) + '\n'
#     elif category == 1:
#         for i in ads:
#             if ad[0] in i and ad[1] in i and ad[4] >= i[4]:
#                 access_landlords.append(i[6].split('"')[1])
#
#         print(ad)
#         for sent in range(len(ad)):
#             msg += f'<b>{repeat_msg_1[1][sent][0]}</b> ' + str(ad[sent]) + '\n'
#
#     return[access_landlords, msg]
#
#
# def send_personal_msg(ad, username, category):
#     if category == 0:
#         ad = remake_ad(ad, username, category)
#         ads = remake_ads(get_ads(person=category), category)
#         send = create_msg(ads, ad, category)
#     elif category == 1:
#         ad = remake_ad(ad, username, category)
#         ads = remake_ads(get_ads(person=category), category)
#         send = create_msg(ads, ad, category)
#     methods(send[0], send[1])
#
# import requests
# from config import token
#
#
# def send_personal_msg(id):
#     params = {
#         'chat_id': id,
#         'text': 'Привет как дела?',
#     }
#
#     response = requests.get('https://api.telegram.org/bot'+token+'/sendMessage', params=params)
#     print(response)
#


