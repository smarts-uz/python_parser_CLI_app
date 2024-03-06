from telebot import TeleBot
from dotenv import load_dotenv
from rich import print
import os
from datetime import datetime
load_dotenv()
TOKEN = os.getenv('token')
chat_id = os.getenv('channel_id')
bot = TeleBot(token=TOKEN)


def send_error_msg(error,group_id=None,tg_channel_id=None):
    match tg_channel_id:
        case None:
            text = f"""|📅{datetime.now()}|🆔{group_id}|
|{error}|"""
        case _:
            text = f"""|📅{datetime.now()}|🆔{tg_channel_id}|
|{error}|"""
    try:
        bot.send_message(chat_id=chat_id,text=text)
        print(f'[orange3]Current Error send to channel successfully')
    except:
        bot.send_message(chat_id=chat_id, text=text)
        print(f'[orange3]Error send to channel')




