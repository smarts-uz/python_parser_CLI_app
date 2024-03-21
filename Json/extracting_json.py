import datetime
import json
import time
from pprint import pprint
import os

from Json.filter_json import filter_message
from Json.json_search import json_search
from django_orm.db.db_functions import insert_or_get_channel, insert_or_get_group
from django_orm.db.db_save import insert_data_to_db
from parsing.file_func.check_file_absent import check_file_absent


def json_extract(path,channel_name,execution_id):
    json_list = json_search(path=path)
    for js in json_list:
        with open(f"{js}", mode='r', encoding='utf-8') as f:
            data = json.load(f)
            data_data = filter_message(datas=data['messages'], path=path, channel_name=channel_name,
                                       execution_id=execution_id)
            # save_info = insert_data_to_db(data_data)
            for channel_data in data_data[0]:
                insert_or_get_channel(channel_data)
            for group_data in data_data[1]:
                insert_or_get_group(group_data)






