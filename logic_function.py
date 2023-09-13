from telebot import types

from config import translator, bot
from questions import repeat_msg_0, repeat_msg_1
from work_with_data import get_lng, update_table, add_lng


def trans(text, lng):
    lang = translator.detect(text).lang
    if type(lang) == list:
        text_trns = translator.translate(text, src=lang[1], dest=lng).text
    else:
        text_trns = translator.translate(text, src=lang, dest=lng).text
    return text_trns


def make_buttons(name, name1, mass, questions, language):
    counter = 0
    questions.update({f'<a href="https://t.me/{name}">{name1}</a>': {}})

    text_trns = trans(mass[0], language)
    ikb_questions = types.InlineKeyboardMarkup()
    for i in mass[1]:
        questions[f'<a href="https://t.me/{name}">{name1}</a>'].update({f'key{counter}': trans(i, language)})
        ikb_questions.add(types.InlineKeyboardButton(trans(i, language), callback_data=f'key{counter}'))
        counter += 1

    return [text_trns, ikb_questions]


def send_questions(message, question, language, questions, l_or_r):
    if l_or_r == 'tenant':
        try:
            if type(question) == list:
                buttons = make_buttons(message.from_user.username,
                                       message.from_user.first_name, question, questions, language)
                bot.send_message(message.chat.id, trans(buttons[0], language), reply_markup=buttons[1])
            else:
                bot.send_message(message.chat.id, trans(question, language))
        except Exception as ex:
            print(ex)
    elif l_or_r == 'landlord':
        try:
            if type(question) == list:
                buttons = make_buttons(message.from_user.username, message.from_user.first_name,
                                       question, questions, language)
                bot.send_message(message.chat.id, trans(buttons[0], language), reply_markup=buttons[1])
            else:
                bot.send_message(message.chat.id,
                                 trans(question, language))
        except Exception as ex:
            print(ex)


def check_ad(message, ad, category, language):
    msg = trans('Давайте проверим ваше объявление перед тем, как я его опубликую👇', language)
    msg += '\n\n'
    print(ad)
    if ad[0] == 'Другой транспорт':
        repeat_msg = repeat_msg_1[2]
        ad_clone = ad
        ad_clone.pop(0)
        for sent in range(len(ad)):
            msg += f'<b>{trans(repeat_msg[sent][0], language)}</b> ' + ad_clone[sent] + '\n'

    elif ad[0] == 'Коммерческая недвижимость':
        repeat_msg = repeat_msg_0[3]
        ad_clone = ad

        for sent in range(len(ad_clone) - 1):
            msg += f'<b>{trans(repeat_msg[sent][0], language)}</b> ' + ad_clone[sent] + '\n'

    else:
        for sent in range(len(ad)):
            if category == 0:
                if len(ad) > 10:
                    msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + ad[sent] + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_0[1][sent][0], language)}</b> ' + ad[sent] + '\n'
            elif category == 1:
                msg += f'<b>{trans(repeat_msg_1[0][sent][0], language)}</b> ' + ad[sent] + '\n'

    ikb4 = types.InlineKeyboardMarkup()
    ikb4.add(types.InlineKeyboardButton(trans('Подтвердить', language), callback_data='access'))
    ikb4.add(types.InlineKeyboardButton(trans('Исправить', language), callback_data='remake'))
    bot.send_message(message.chat.id, msg, parse_mode="HTML", reply_markup=ikb4)


def photo_check(category, ad, language):
    msg = trans('Давайте проверим ваше объявление перед тем, как я его опубликую👇', language)
    msg += '\n\n'

    if category == 1:
        repeat_msg = repeat_msg_1[2]
        ad_clone = ad
        ad_clone.pop(0)

        for sent in range(len(ad_clone) - 1):
            msg += f'<b>{trans(repeat_msg[sent][0], language)}</b> ' + ad_clone[sent] + '\n'

    elif category == 0:
        repeat_msg = repeat_msg_0[2]
        ad_clone = ad
        # ad_clone.pop(0)

        for sent in range(len(ad_clone) - 1):
            msg += f'<b>{trans(repeat_msg[sent][0], language)}</b> ' + ad_clone[sent] + '\n'

    return msg


def send_ad_first_tenant(call, l_or_r, category, ads, language):
    print(category)
    print(l_or_r)
    if len(ads) == 0:
        yes_or_no = types.InlineKeyboardMarkup()
        yes_or_no.add(types.InlineKeyboardButton(trans('Да', language), callback_data='Yes'))
        yes_or_no.add(types.InlineKeyboardButton(trans('Нет', language), callback_data='No'))
        bot.send_message(call.message.chat.id, ' Пока таких объявлений нет.\nХотите изменить фильтры?',
                         reply_markup=yes_or_no)
    print(ads)
    for ad in ads:
        photo4 = None
        if l_or_r == 'tenant':
            if category == 0:
                photo4 = open(f'{ad[12]}', "rb")
            elif category == 1:
                photo4 = open(f'{ad[7]}', "rb")

        msg = '#Cдам\n\n'

        if category == 0 and ad[0] == 'Коммерческая недвижимость':
            print(ad)
            clone_ad = []
            for i in ad:
                if not i:
                    continue
                else:
                    clone_ad.append(i)
            print(clone_ad)
            for sent in range(len(clone_ad) - 2):
                msg += f'<b>{trans(repeat_msg_0[2][sent][0], language)}</b> ' + trans(str(clone_ad[sent]), language) + '\n'

        elif category == 0:
            for sent in range(len(ad) - 2):
                if sent == 9 or sent == 11:
                    msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + trans(str(ad[sent]), language) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + trans(ad[sent], language) + '\n'

        elif category == 1 and ad[0] == 'Другой Транспорт':
            print(ad)
            ad.pop(0)
            for sent in range(len(ad) - 2):
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + trans(str(ad[sent]), language) + '\n'
                print(msg)
        elif category == 1:
            for sent in range(len(ad) - 2):
                if sent == 1:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + \
                           trans(ad[sent], language) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + trans(ad[sent], language) + '\n'

        ad_button = types.InlineKeyboardMarkup()
        ad_button.add(types.InlineKeyboardButton(trans('Главное меню', language), callback_data='back_menu1'))

        bot.send_photo(call.message.chat.id, photo4, caption=msg, reply_markup=ad_button, parse_mode='HTML')


def send_ad_first_landlord(call, category, ads, language):
    if len(ads) == 0:
        yes_or_no = types.InlineKeyboardMarkup()
        yes_or_no.add(types.InlineKeyboardButton(trans('Да', language), callback_data='Yes'))
        yes_or_no.add(types.InlineKeyboardButton(trans('Нет', language), callback_data='No'))
        bot.send_message(call.message.chat.id, ' Пока таких объявлений нет.\nХотите изменить фильтры?',
                         reply_markup=yes_or_no)
    for ad in ads:

        msg = '#Арендую\n\n'

        if category == 0 and ad[0] == 'Коммерческая недвижимость':
            print(ad)
            clone_ad = []
            for i in ad:
                if not i:
                   continue
                else:
                    clone_ad.append(i)

            print(clone_ad)
            for sent in range(len(clone_ad) - 1):
                msg += f'<b>{trans(repeat_msg_0[2][sent][0], language)}</b> ' + trans(str(clone_ad[sent]), language) + '\n'

        elif category == 0:
            print(f'0 -> {ad}')
            clone_ad = []
            for i in ad:
                if not i:
                    continue
                else:
                    clone_ad.append(i)
            print(f'0 -> {clone_ad}')
            for sent in range(len(clone_ad) - 1):
                if sent == 9:
                    msg += f'<b>{trans(repeat_msg_0[1][sent][0], language)}</b> ' + trans(str(clone_ad[sent]), language) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_0[1][sent][0], language)}</b> ' + trans(clone_ad[sent], language) + '\n'

        elif category == 1 and ad[0] == 'Другой Транспорт':
            ad.pop(0)
            for sent in range(len(ad)):
                msg += f'<b>{trans(repeat_msg_1[2][sent][0], language)}</b> ' + trans(str(ad[sent]), language) + '\n'
        elif category == 1:
            for sent in range(len(ad)):
                if sent == 2 or sent == 6:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + trans(ad[sent], language) + '\n'
                else:
                    msg += f'<b>{trans(repeat_msg_1[1][sent][0], language)}</b> ' + trans(ad[sent], language) + '\n'

        ad_button = types.InlineKeyboardMarkup()
        ad_button.add(types.InlineKeyboardButton(trans('Главное меню', language), callback_data='back_menu1'))

        bot.send_message(call.message.chat.id, msg, reply_markup=ad_button, parse_mode='HTML')


def send_ad(call, mass_buttons, mass_buttons1, l_or_r, counter, category, ads, language):
    photo5 = None
    if l_or_r == 'tenant':
        if category == 0:
            photo5 = open(f'{ads[counter][12]}', "rb")
            mass = ads[counter][0:12]
        elif category == 1:
            photo5 = open(f'{ads[counter][7]}', "rb")
            mass = ads[counter][0:7]
    else:
        mass = ads[counter]

    msg = ''

    for sent in range(len(mass)):
        if category == 0:
            if sent == 9 or sent == 11:
                msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + \
                       ads[counter][sent] + '\n'
            else:
                msg += f'<b>{trans(repeat_msg_0[0][sent][0], language)}</b> ' + trans(
                    ads[counter][sent],
                    language) + '\n'
        elif category == 1:
            if sent == 1:
                msg += f'<b>{trans(repeat_msg_1[0][sent][0], language)}</b> ' + \
                       ads[counter][sent] + '\n'
            else:
                msg += f'<b>{trans(repeat_msg_1[0][sent][0], language)}</b> ' + trans(
                    ads[counter][sent],
                    language) + '\n'
    if l_or_r == 'tenant':
        if len(ads) == counter:
            ikb3 = types.InlineKeyboardMarkup(mass_buttons1)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(call.message.chat.id, photo5, caption=msg, reply_markup=ikb3, parse_mode='HTML')
        elif 1 == counter:
            ikb3 = types.InlineKeyboardMarkup(mass_buttons1)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(call.message.chat.id, photo5, caption=msg, reply_markup=ikb3, parse_mode='HTML')
        else:
            ikb3 = types.InlineKeyboardMarkup(mass_buttons)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_photo(call.message.chat.id, photo5, caption=msg, reply_markup=ikb3, parse_mode='HTML')
    else:
        if len(ads) == counter:
            ikb3 = types.InlineKeyboardMarkup(mass_buttons1)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, msg, reply_markup=ikb3, parse_mode='HTML')
        else:
            ikb3 = types.InlineKeyboardMarkup(mass_buttons)
            bot.delete_message(call.message.chat.id, call.message.message_id)
            bot.send_message(call.message.chat.id, msg, reply_markup=ikb3, parse_mode='HTML')


def set_language(message, language_chk, lng):
    if language_chk == 0:
        add_lng(f'<a href="https://t.me/{message.from_user.username}">{message.from_user.first_name}</a>', lng)
        bot.send_message(message.chat.id, 'Язык был успешно изменен')
    else:
        update_table('languages', 'language', lng,
                     f'<a href="https://t.me/{message.from_user.username}">{message.from_user.first_name}</a>')

    language = get_lng(f'<a href="https://t.me/{message.from_user.username}">{message.from_user.first_name}</a>')

    ikb = types.InlineKeyboardMarkup()
    # ikb.add(types.InlineKeyboardButton(trans('Недвижимость', language), callback_data='realty'))
    # ikb.add(types.InlineKeyboardButton(trans('Транспорт', language), callback_data='transport'))
    ikb.add(types.InlineKeyboardButton(trans('Услуги', language), callback_data='services'))
    # ikb.add(types.InlineKeyboardButton(trans('Медицина', language), callback_data='medicines'))
    # ikb.add(types.InlineKeyboardButton(trans('Выполняю/Покупаю услуги', language), callback_data='do_buy'))

    text_trns = trans('Выберите категорию: ', language)
    bot.send_message(message.chat.id, text_trns, reply_markup=ikb)


def filters_(category, language, call):

    if category == 1:
        check_ad = types.InlineKeyboardMarkup()
        check_ad.add(types.InlineKeyboardButton(trans('Авто', language),
                                                callback_data='Авто'))
        check_ad.add(types.InlineKeyboardButton(trans('Мопед/Мотоцикл', language),
                                                callback_data='Мопед/Мотоцикл'))
        check_ad.add(types.InlineKeyboardButton(trans('Другой транспорт', language),
                                                callback_data='Другой транспорт'))
        check_ad.add(types.InlineKeyboardButton(trans('Посмотреть все объявления', language),
                                                callback_data='check_all'))

        bot.send_message(call.message.chat.id, trans('Выберите пункт ниже:', language),
                         reply_markup=check_ad)
    elif category == 0:
        check_ad = types.InlineKeyboardMarkup()
        check_ad.add(types.InlineKeyboardButton(trans('Кондо', language),
                                                callback_data='Кондо'))
        check_ad.add(types.InlineKeyboardButton(trans('Вилла', language),
                                                callback_data='Вилла'))
        check_ad.add(types.InlineKeyboardButton(trans('Коммерческая недвижимость', language),
                                                callback_data='Коммерческая_недвижимость'))
        check_ad.add(types.InlineKeyboardButton(trans('Посмотреть все объявления', language),
                                                callback_data='check_all'))

        bot.send_message(call.message.chat.id, trans('Выберите пункт ниже:', language),
                         reply_markup=check_ad)

