import os

import natsort

from Json.json_search import json_search

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from rich import print
from pprint import pprint
from django_orm.db.db_functions import insert_or_get_channel, insert_or_get_group, change_status_execution, \
    get_status_execution
from parsing.other_functions import folder_path, search_message_html
from django_orm.db.models import *


def insert_data_to_db(info_list):
    global  ex_id
    channel_count = [0,0]
    group_count = [0,0]
    for data_ch in info_list[0]:
        for data_c in data_ch:
            channel = insert_or_get_channel(data_c)
            exist_c = channel[0]
            new_c = channel[1]
            channel_count[0] += exist_c
            channel_count[1] += new_c


    for data_gr in info_list[1]:
        for data_g in data_gr:
            group = insert_or_get_group(data_g)
            exist_g = group[0]
            new_g = group[1]
            ex_id = group[2]
            group_count[0]+=exist_g
            group_count[1]+=new_g
    try:
        change_status_execution(id=ex_id, parsing_ok=True)
    except:
        print('Nothing to parser')
    return channel_count,group_count






def channel_add_db(data:dict):
    for msg_c in data:
        print(msg_c['message_detail'])
        insert_or_get_channel(msg_c)





def group_add_db(data:dict):

    # for msg in data:
    #     print(msg,'123')
    #     # print(msg['message_detail'])
    insert_or_get_group(data)



def insert_or_get_execution(path:str,name:str):
    paths = search_message_html(path)
    exist_count = 0
    new_count = 0
    ex_ids = []
    for path in paths:
        pth = folder_path(path)
        try:
            execute = Execution.objects.get(path=pth)
            exist_count += 1
            ex_ids.append({
                "id":execute.pk,
                "name":name,
                "path":pth,
                "status":execute.status
            })
            print(f'[pink]{pth} : this path already exist with id: {execute.pk} and [green]status: {execute.status} ')
        except Execution.DoesNotExist:

            execute = Execution.objects.create(
            name=name,
            path=pth,
            status='new'
        )
            ex_ids.append({
                "id": execute.pk,
                "name": name,
                "path": pth,
                "status": "new"
            })
            new_count += 1
            print(f'[green1]{pth} : new added to db with id: {execute.pk}')

    print(f'Exist count: {exist_count}')
    print(f'New count: {new_count}')
    return natsort.os_sorted(ex_ids)



def insert_or_get_execution_json(path,name):
    paths = json_search(path)
    exist_count = 0
    new_count = 0
    ex_ids = []
    for path in paths:
        pth = folder_path(path)
        try:
            execute = Execution.objects.get(path=pth)
            exist_count += 1
            ex_ids.append({
                "id": execute.pk,
                "name": name,
                "path": pth,
                "status": execute.status
            })
            print(f'[pink]{pth} : this path already exist with id: {execute.pk} and [green]status: {execute.status} ')
        except Execution.DoesNotExist:

            execute = Execution.objects.create(
                name=name,
                path=pth,
                status='new'
            )
            ex_ids.append({
                "id": execute.pk,
                "name": name,
                "path": pth,
                "status": "new"
            })
            new_count += 1
            print(f'[green1]{pth} : new added to db with id: {execute.pk}')

    print(f'Exist count: {exist_count}')
    print(f'New count: {new_count}')
    return natsort.os_sorted(ex_ids)

# insert_or_get_execution("h:\Exports\SmartTech Learning Group",'SmartTech Learning')
