import sys

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from rich import print

sys.dont_write_bytecode = True
from parsing.functions import correct_time_data
from django_orm.db.models import *
from django_orm.db.save_to_db import update_db
from rich import print
from log3 import Logger

statistic = Logger('statictics', 'a')

def channel_content_db_add(dict_1):
    for i, k in dict_1.items():
        try:
            from_name = k[2]
        except:
            from_name = 'Admin'
        text = k[0]
        data_time = correct_time_data(k[1])
        main_folder_name = k[-1]
        msg_id = i
        data = {'from_name': from_name, 'text': text, 'date': data_time, 'message_id': msg_id, 'main_folder_name': main_folder_name}
        my_model_instance = TgChannel(**data)
        my_model_instance.save()
        msg = f'{text} - has added to channel_content!'
        statistic.log(msg)
        print(f'[bright_cyan]{msg}')


def group_content_db_add(list2):
    for i in list2:
        from_name = i[0]
        text = i[1]
        content = i[2]
        data_title = i[3]
        message_details = i[4]
        msg_id = i[5]
        replied_message_details = i[6]
        reply_id = i[7]
        joined = i[8]
        type_of_content = i[-2]
        file_path = i[-1]
        if len(i) == 12:
            description = i[9]
            video_duration = i[10]
        else:
            description = None
            video_duration = None
        data = {'channel_text': text, 'content': content, 'date': data_title,
                'message_details': message_details, 'message_id': msg_id, 'replied_message_details': replied_message_details,
                'replied_message_id': reply_id, 'joined': joined, 'type': type_of_content, 'description': description, 'video_duration': video_duration, 'filepath':file_path}

        my_model_instance = TgGroup(**data)
        my_model_instance.save()
        msg = f"{content} - has added to group_content!"
        statistic.log(msg)
        print(f'[bright_cyan]{msg}')


def save_data_to_db(info_list):

    for i in info_list[0]:
        channel_content_db_add(i)
    for k in info_list[1]:
        group_content_db_add(k)


def update_database():
    update_db()



