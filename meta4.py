import time
from time import sleep
import clipboard

import telebot
import pyautogui
from bottons import *
import random


def generate_random_code():
    code = ''.join(random.choices('0123456789', k=6))
    return code


def generate_random_codeMT5():
    code = ''.join(random.choices('0123456789', k=6))
    return code



names = [
    "traderone", "tradeone", "tradersone", "onetrader", "onetraderone", "propone", "oneprop", "traderprop",
    "tradersprop", "traderprops"
]

bot_token = "7130664339:AAFkbRrAeTE7OXbgcv8X-GHqaZydT3S6Cs8"
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "choose your broker", reply_markup=get_main_buttons())


@bot.message_handler(func=lambda message: True)
def forex(message):
    if message.text == "roboforexMT4":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_robo4())
    elif message.text == "AlpariMT4":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_alpari4())
    elif message.text == "Forex4uMT4":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_forex4u4())
    elif message.text == "AlpariMT5":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_alpari5())
    elif message.text == "Forex4uMT5":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_forex4u5())

######################################
#
#
#
##         MT4
#
#
#
@bot.callback_query_handler(func=lambda call: call.data.startswith("robo"))
def handle_buy_callback(call):
    bot.send_message(call.message.chat.id, "waiting")
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("roboForex MT4")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.press('f')
    pyautogui.keyUp('alt')  # Optional
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    time.sleep(0.3)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    code = generate_random_code()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write("+1")
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write(code)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    balance = "0"
    if call.data == "roboMT45k":
        balance = "5000"
    elif call.data == "roboMT410k":
        balance = "10000"
    elif call.data == "roboMT415k":
        balance = "15000"
    elif call.data == "roboMT425k":
        balance = "25000"
    else:
        bot.send_message(call.message.chat.id, "Sorry I didn't understand")
        return False

    pyautogui.write(balance)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.click(x=815, y=654)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(4)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    password = clipboard.paste()
    print(password)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    username = clipboard.paste()
    print(username)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    broker = call.data
    if username and password is not None:
        bot.send_message(call.message.chat.id,
                         f'broker with balance = {broker} \n username = {username} \n password = {password}',
                         reply_markup=get_main_buttons())

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')  # Optional


@bot.callback_query_handler(func=lambda call: call.data.startswith("alpariMT4"))
def handle_buy_callback(call):
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("Alpari MT4")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(x=22, y=45)
    time.sleep(0.5)
    pyautogui.click(x=22, y=187)

    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    code = generate_random_code()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write("+1")
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write(code)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    balance = "0"
    if call.data == "alpariMT45k":
        balance = "5000"
    elif call.data == "alpariMT410k":
        balance = "10000"
    elif call.data == "alpariMT415k":
        balance = "15000"
    elif call.data == "alpariMT425k":
        balance = "25000"
    else:
        bot.send_message(call.message.chat.id, "Sorry I didn't understand")
        return False

    pyautogui.write(balance)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.click(x=815, y=654)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(4)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    password = clipboard.paste()
    print(password)
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    username = clipboard.paste()
    print(username)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    broker = call.data
    if username and password is not None:
        bot.send_message(call.message.chat.id,
                         f'broker with balance = {broker} \n username = {username} \n password = {password}',
                         reply_markup=get_main_buttons())

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')  # Optional


@bot.callback_query_handler(func=lambda call: call.data.startswith("forex4uMT4"))
def handle_buy_callback(call):
    bot.send_message(call.message.chat.id, "waiting")
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("Forex4you")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(x=22, y=45)
    time.sleep(0.5)
    pyautogui.click(x=22, y=187)

    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    code = generate_random_code()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write("+1")
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write(code)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    balance = "0"
    if call.data == "forex4uMT45k":
        balance = "5000"
    elif call.data == "forex4uMT410k":
        balance = "10000"
    elif call.data == "forex4uMT415k":
        balance = "15000"
    elif call.data == "forex4uMT425k":
        balance = "25000"
    else:
        bot.send_message(call.message.chat.id, "Sorry I didn't understand")
        return False

    time.sleep(0.5)
    print(balance)
    pyautogui.write(balance)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.click(x=815, y=654)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(4)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    password = clipboard.paste()
    print(password)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    username = clipboard.paste()
    print(username)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    broker = call.data
    if username and password is not None:
        bot.send_message(call.message.chat.id,
                         f'broker with balance = {broker} \n username = {username} \n password = {password}',
                         reply_markup=get_main_buttons())

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')  # Optional


###################################################################
#
#
#                MT5
##
#


@bot.callback_query_handler(func=lambda call: call.data.startswith("alpariMT5"))
def handle_buy_callback(call):
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("Alpari MT5")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.keyDown('alt')
    pyautogui.press('f')
    pyautogui.keyUp('alt')  # Optional
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.press('down')
    time.sleep(0.3)
    pyautogui.hotkey('enter')
    time.sleep(0.3)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    pyautogui.write(random_name)
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    code = generate_random_codeMT5()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.write(f'7161{code}')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.press('down')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)


    balance = "0"
    if call.data == "alpariMT55k":
        balance = "5000"
    elif call.data == "alpariMT510k":
        balance = "10000"
    elif call.data == "alpariMT515k":
        balance = "15000"
    elif call.data == "alpariMT525k":
        balance = "25000"
    else:
        bot.send_message(call.message.chat.id, "Sorry I didn't understand")
        return False

    pyautogui.write(balance)
    pyautogui.hotkey('tab')

    time.sleep(0.5)
    pyautogui.click(x=740, y=667)
    time.sleep(2)
    pyautogui.hotkey('tab')
    time.sleep(0.5)

    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(4)
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'c')
    # password = clipboard.paste()
    # print(password)
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(x=813, y=610)
    time.sleep(1)
    data = clipboard.paste()
    print(data)
    # time.sleep(0.5)
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    #
    # pyautogui.hotkey('tab')
    # time.sleep(0.5)
    # pyautogui.hotkey('enter')
    broker = call.data
    if data is not None:
        bot.send_message(call.message.chat.id,
                         f'{data}',
                         reply_markup=get_main_buttons())

    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')  # Optional


















bot.infinity_polling(skip_pending=True)
