import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from rich import print
from pprint import pprint
from django_orm.db.db_functions import insert_or_get_channel, insert_or_get_group
from parsing.other_functions import folder_path, search_message_html
from django_orm.db.models import *


# def smth():
#     fname_list = search_html(path)
#     channel_content_list = []
#     group_content_list = []
#
#     for folder in fname_list:
#         f_path = folder_path(folder)
#         parsing = Pars(folder)
#         main_folder_name = parsing.parsing()[2]
#         ready_information = parsing.joined_messages()
#         channel_content = parsing.main_msg()
#         channel_content_list.append(channel_content)
#         group_content_list.append(ready_information)
#
#         save_to_execution(name=main_folder_name, path=f_path, status='in_process')
#
#     return [channel_content_list, group_content_list]
#
# def save_to_execution(name,path,status):
#     try:
#         execute = Execution.objects.get(path=path)
#         print('this path already exists!!')
#     except Execution.DoesNotExist:
#         execute = Execution.objects.create(
#             name = name,
#             path = path,
#             status = status
#         )
#         print(f'{path} saved to Execution table')

def insert_data_to_db(info_list):
    channel_count = [0,0]
    group_count = [0,0]
    for data_c in info_list[0][0]:
        channel = insert_or_get_channel(data_c)
        exist_c = channel[0]
        new_c = channel[1]
        channel_count[0]+=exist_c
        channel_count[1]+=new_c

    for data_g in info_list[1][0]:
        group = insert_or_get_group(data_g)
        exist_g = group[0]
        new_g = group[1]
        group_count[0]+=exist_g
        group_count[1]+=new_g


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
    for path in paths:
        pth = folder_path(path)
        try:
            execute = Execution.objects.get(path=pth)
            exist_count += 1
            print(f'[{pth}] this path already exist with [blue]id: {execute.pk} and [green]status: {execute.status} ')
        except Execution.DoesNotExist:

            execute = Execution.objects.create(
            name=name,
            path=pth,
            status='new'
        )
            new_count += 1
            print(f'{pth} : new added to db with id: {execute.pk}')

    print(f'Exist count: {exist_count}')
    print(f'New count: {new_count}')


# insert_or_get_execution("h:\Exports\SmartTech Learning Group",'SmartTech Learning')
