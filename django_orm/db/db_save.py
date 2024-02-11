import os
from rich import print
from pprint import pprint

from django_orm.db.db_functions import insert_or_get_channel, insert_or_get_group

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()

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

    for i in info_list[0]:
        channel_add_db(i)
    for k in info_list[1]:
        group_add_db(k)



def channel_add_db(data):
    for msg_c in data[0]:
        insert_or_get_channel(msg_c)
    for msg_g in data[1]:
        insert_or_get_group(msg_g)







def group_add_db(data):
    for msg in data:
        insert_or_get_group(msg)



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
