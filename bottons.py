from telebot import types


def get_main_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    buttons = [
        types.KeyboardButton("Alpari"),
        types.KeyboardButton("Forex4u"),
        types.KeyboardButton("roboforex"),

    ]
    markup.add(*buttons)
    return markup


def balance_robo():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="robo5k"),
        types.InlineKeyboardButton("10k", callback_data="robo10k"),
        types.InlineKeyboardButton("15k", callback_data="robo15k"),
        types.InlineKeyboardButton("25k", callback_data="robo25k"),
    ]
    markup.add(*buttons)
    return markup


def balance_alpari():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="alpari5k"),
        types.InlineKeyboardButton("10k", callback_data="alpari10k"),
        types.InlineKeyboardButton("15k", callback_data="alpari15k"),
        types.InlineKeyboardButton("25k", callback_data="alpari25k"),
    ]
    markup.add(*buttons)
    return markup



def balance_forex4u():
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [
        types.InlineKeyboardButton("5k", callback_data="forex4u5k"),
        types.InlineKeyboardButton("10k", callback_data="forex4u10k"),
        types.InlineKeyboardButton("15k", callback_data="forex4u15k"),
        types.InlineKeyboardButton("25k", callback_data="forex4u25k"),
    ]
    markup.add(*buttons)
    return markup
