import time

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
            match group_id:
                case None:
                    text = f"""|⚠️ {error} |"""
                case _:
                    text = f"""|🆔 {group_id} |
|⚠️ {error} |"""
        case _:
            text = f"""|🆔{tg_channel_id} |
|⚠️ {error} |"""

    try:
        bot.send_message(chat_id=chat_id,text=text)
        time.sleep(1.2)
        print(f'[orange3]Current Error send to channel successfully')
    except:
        bot.send_message(chat_id=chat_id, text=text)
        time.sleep(1.2)
        print(f'[orange3]Error send to channel')





