import sys
sys.dont_write_bytecode = True
from parsing.functions import correct_time_data
# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from parsing.functions import logger_path
import logging
from rich import print
import django
django.setup()
from django_orm.db.models import *
from django_orm.db.save_to_db import update_db
module_name = os.path.splitext(os.path.basename(__file__))[0]
logging.basicConfig(level=logging.INFO,format="%(name)s %(asctime)s %(levelname)s %(message)s", filename=f"{logger_path()}/{module_name}.log",filemode="a")

def channel_content_db_add(dict_1):
    for i, k in dict_1.items():
        try:
            from_name = k[2]
        except:
            from_name = 'SmartTech Learning'
        text = k[0]
        data_time = correct_time_data(k[1])
        msg_id = i
        data = {'from_name': from_name, 'text': text, 'data': data_time, 'message_id': msg_id}
        my_model_instance = channel_content(**data)
        my_model_instance.save()
        print(f'{text} - has added to channel_content!')
        logging.info(f'{text} - has added to channel_content!')


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
        type_of_content = i[-1]
        if len(i) == 12:
            description = i[9]
            video_duration = i[10]
        else:
            description = None
            video_duration = None
        data = {'from_name': from_name, 'channel_text': text, 'content': content, 'data': data_title,
                'message_details': message_details, 'message_id': msg_id, 'replied_message_details': replied_message_details,
                'replied_message_id': reply_id, 'joined': joined, 'type': type_of_content, 'description': description, 'video_duration': video_duration}
        my_model_instance = group_content(**data)
        my_model_instance.save()
        print(f"{content} - has added to group_content!")
        logging.info(f"{content} - has added to group_content!")


def save_data_to_db(info_list):
    for i in info_list[0]:
        channel_content_db_add(i)
    for k in info_list[1]:
        group_content_db_add(k)


def update_database():
    update_db()
