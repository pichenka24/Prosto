from config import bot, translator
from questions import repeat_msg_0, repeat_msg_1
from telebot import types


def trans(text, language):
    text_trns = translator.translate(text, src='ru', dest=language).text
    return text_trns


def ad_from_tenant(call, ad, category, username, language):
    link = None
    if category == 0:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление',  url='t.me/Kilimandzharo_bot?start=realty'))
    elif category == 1:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление', url='t.me/Kilimandzharo_bot?start=transport'))
    elif category == 2:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление', url='t.me/Kilimandzharo_bot?start=services'))

    msg = '#Арендую\n\n'

    mass = ad
    mass.append(username)
    if category == 0 and ad[0] == 'Коммерческая недвижимость':
        print(f'in func -> {ad}')
        for sent in range(len(mass)):
            msg += f'<b>{trans(repeat_msg_0[3][sent][0], language)}</b> ' + str(mass[sent]) + '\n'

    elif category == 1 and len(ad) == 6:
        for sent in range(len(mass)):
            if sent == 5:
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
            else:
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
    elif category == 1 and ad[0] == 'Мопед/Мотоцикл':
        mass.pop(1)
        for sent in range(len(mass)):
            if sent == 5:
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
            else:
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'

    elif category == 2:
        msg = trans(f'#ОкажуУслугу\n#{ad[0].replace(" ", "")}', language)
        msg += '\n\n'
        msg += ad[1]
        msg += f'\n\n{trans("Контакт: ", language)}{username}'

    else:
        for sent in range(len(mass)):
            if category == 0:
                if sent == 9:
                    msg += f'<b>{trans(repeat_msg_0[1][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_0[1][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
            elif category == 1:
                if sent == 2 or sent == 6:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + str(mass[sent]) + '\n'

    back = types.InlineKeyboardMarkup()
    back.add(types.InlineKeyboardButton(trans('Главое Меню', language), callback_data='back_menu1'))

    if category == 0:
        msg_link = bot.send_message(chat_id=-1001901862304, text=msg, parse_mode='HTML',
                         reply_markup=link, reply_to_message_id=415)

        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/415/{msg_link.id}', reply_markup=back)
        print(msg_link)
    elif category == 1:
        msg_link = bot.send_message(chat_id=-1001901862304, text=msg, parse_mode='HTML',
                         reply_markup=link, reply_to_message_id=414)

        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/414/{msg_link.id}', reply_markup=back)

    elif category == 2:
        msg_link = bot.send_message(chat_id=-1001901862304, text=msg, parse_mode='HTML',
                                    reply_markup=link, reply_to_message_id=528)

        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/528/{msg_link.id}', reply_markup=back)


def ad_from_landlord(call, category, ad, username, language):
    print(category, ad, username, language)
    mass = ad
    photo4 = None
    if category == 0 and len(mass) == 7:
        photo4 = open(f'{mass[6]}', "rb")
        mass.pop(0)
        mass.pop(5)
        mass.append(username)
    elif category == 0:
        photo4 = open(f'{mass[12]}', "rb")
        mass.pop(0)
        mass.pop(11)
        mass.append(username)
    elif category == 1 and len(ad) == 7:
        photo4 = open(f'{mass[6]}', "rb")
        mass.pop(0)
        mass.pop(5)
        mass.append(username)
    elif category == 1 and ad[1] == 'Мопед/Мотоцикл':
        photo4 = open(f'{mass[7]}', "rb")
        mass.pop(0)
        mass.pop(1)
        mass.pop(5)
        mass.append(username)
    elif category == 1:
        photo4 = open(f'{mass[7]}', "rb")
        mass.pop(0)
        mass.pop(6)
        mass.append(username)

    msg = '#Cдам\n\n'
    print(ad)

    link = None
    if category == 0:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление',  url='t.me/Kilimandzharo_bot?start=realty'))
    elif category == 1:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление', url='t.me/Kilimandzharo_bot?start=transport'))
    elif category == 2:
        link = types.InlineKeyboardMarkup()
        link.add(types.InlineKeyboardButton(text='Разместить/Найти объявление', url='t.me/Kilimandzharo_bot?start=services'))

    if category == 1 and len(ad) == 6:
        for sent in range(len(mass)):
            if sent == 5:          msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
            else:
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
    elif category == 0 and len(ad) == 6:
        for sent in range(len(mass)):
            msg += f'<b>{trans(repeat_msg_0[2][sent][0], language)}</b> ' + str(mass[sent]) + '\n'

    elif category == 2:
        msg = trans(f'#ИщуУслугу\n#{ad[0].replace(" ", "")}', language)
        msg += '\n\n'
        msg += ad[1]
        msg += f'\n\n{trans("Контакт: ", language)}{username}'

        print(msg)

    else:
        for sent in range(len(mass)):
            if category == 0:
                if sent == 9 or sent == 11:
                    msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
            elif category == 1:
                if sent == 1:
                    msg += f'<b>{trans(repeat_msg_1[0][sent][0], language)}</b> ' + str(mass[sent]) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_1[0][sent][0], language)}</b> ' + str(mass[sent]) + '\n'

    back = types.InlineKeyboardMarkup()
    back.add(types.InlineKeyboardButton(trans('Главое Меню', language), callback_data='back_menu1'))

    if category == 0:
        msg_link = bot.send_photo(chat_id=-1001901862304, photo=photo4, caption=msg, parse_mode='HTML',
                       reply_markup=link, reply_to_message_id=415)
        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/415/{msg_link.id}', reply_markup=back)
    elif category == 1:
        msg_link = bot.send_photo(chat_id=-1001901862304, photo=photo4, caption=msg, parse_mode='HTML',
                       reply_markup=link, reply_to_message_id=414)
        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/414/{msg_link.id}', reply_markup=back)
    elif category == 2:

        msg_link = bot.send_message(chat_id=-1001901862304, text=msg, parse_mode='HTML',
                                    reply_markup=link, reply_to_message_id=528)

        bot.send_message(call.message.chat.id,
                         trans('Ваше объявление добавлено!\nВы можете его найти по ссылке -> \n', language)
                         + f'https://t.me/Hua_Hin_bit/528/{msg_link.id}', reply_markup=back)

