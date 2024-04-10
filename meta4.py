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
    if message.text == "roboforex":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_robo())
    elif message.text == "Alpari":
        bot.send_message(message.chat.id, "choose your balance", reply_markup=balance_alpari())


@bot.callback_query_handler(func=lambda call: call.data.startswith("robo"))
def handle_buy_callback(call):
    bot.send_message(call.message.chat.id, "waiting")
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("roboForex MT4")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(x=22, y=45)
    time.sleep(1)
    pyautogui.click(x=22, y=187)

    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    code = generate_random_code()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.write("+1")
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.write(code)
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    balance = "0"
    if call.data == "robo5k":
        balance = "5000"
    elif call.data == "robo10k":
        balance = "10000"
    elif call.data == "robo15k":
        balance = "15000"
    elif call.data == "robo25k":
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


@bot.callback_query_handler(func=lambda call: call.data.startswith("alpari"))
def handle_buy_callback(call):
    pyautogui.hotkey('win')
    time.sleep(2)
    pyautogui.write("Alpari MT4")
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(5)
    pyautogui.click(x=22, y=45)
    time.sleep(1)
    pyautogui.click(x=22, y=187)

    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    random_name = random.choice(names)
    pyautogui.write(random_name)
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    code = generate_random_code()
    pyautogui.write(f'{random_name}.{code}@gmail.com')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.write("+1")
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.write(code)
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    pyautogui.hotkey('tab')
    time.sleep(0.5)
    balance = "0"
    if call.data == "alpari5k":
        balance = "5000"
    elif call.data == "alpari10k":
        balance = "10000"
    elif call.data == "alpari15k":
        balance = "15000"
    elif call.data == "alpari25k":
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


bot.infinity_polling(skip_pending=True)
