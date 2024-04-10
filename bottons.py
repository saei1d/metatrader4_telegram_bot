from telebot import types


def get_main_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [
        types.KeyboardButton("AlpariMT4"),
        types.KeyboardButton("Forex4uMT4"),
        types.KeyboardButton("roboforexMT4"),
        types.KeyboardButton("AlpariMT5"),
        types.KeyboardButton("Forex4uMT5"),
        types.KeyboardButton("roboforexMT5"),

    ]
    markup.add(*buttons)
    return markup


def balance_robo4():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="roboMT45k"),
        types.InlineKeyboardButton("10k", callback_data="roboMT410k"),
        types.InlineKeyboardButton("15k", callback_data="roboMT415k"),
        types.InlineKeyboardButton("25k", callback_data="roboMT425k"),
    ]
    markup.add(*buttons)
    return markup


def balance_alpari4():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="alpariMT45k"),
        types.InlineKeyboardButton("10k", callback_data="alpariMT410k"),
        types.InlineKeyboardButton("15k", callback_data="alpariMT415k"),
        types.InlineKeyboardButton("25k", callback_data="alpariMT425k"),
    ]
    markup.add(*buttons)
    return markup


def balance_forex4u4():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="forex4uMT45k"),
        types.InlineKeyboardButton("10k", callback_data="forex4uMT410k"),
        types.InlineKeyboardButton("15k", callback_data="forex4uMT415k"),
        types.InlineKeyboardButton("25k", callback_data="forex4uMT425k"),
    ]
    markup.add(*buttons)
    return markup


#
#
#               👇MT5
#
#
#

def balance_alpari5():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="alpariMT55k"),
        types.InlineKeyboardButton("10k", callback_data="alpariMT510k"),
        types.InlineKeyboardButton("15k", callback_data="alpariMT515k"),
        types.InlineKeyboardButton("25k", callback_data="alpariMT525k"),
    ]
    markup.add(*buttons)
    return markup


def balance_forex4u5():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="forex4uMT55k"),
        types.InlineKeyboardButton("10k", callback_data="forex4uMT510k"),
        types.InlineKeyboardButton("15k", callback_data="forex4uMT515k"),
        types.InlineKeyboardButton("25k", callback_data="forex4uMT525k"),
    ]
    markup.add(*buttons)
    return markup


def balance_icmarketsMT5():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="icmarketsMT55k"),
        types.InlineKeyboardButton("10k", callback_data="icmarketsMT510k"),
        types.InlineKeyboardButton("15k", callback_data="icmarketsMT515k"),
        types.InlineKeyboardButton("25k", callback_data="icmarketsMT525k"),
    ]
    markup.add(*buttons)
    return markup
