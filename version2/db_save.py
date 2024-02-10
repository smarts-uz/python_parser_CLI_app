import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()


from pyfiglet import Figlet
from parsing.functions import search_html
from version2.other_functions import folder_path, search_message_html
from django_orm.db.models import *
import sys


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


#
# def channel_add_db(data):
#     for msg in data:
#         msg['execution_id'] = get_execution_id(msg['path'])
#         try:
#             tg_channels = TgChannel.objects.get(**msg)
#
#         except TgChannel.DoesNotExist:
#             channel = TgChannel.objects.create(**msg)
#             print(f'{msg["message_id"]} saved to db channel')


#
# def group_add_db(data):
#     for msg in data:
#         msg["tg_channel_id"] = get_channel_id(msg['replied_message_id'])
#         msg['execution_id'] = get_execution_id(msg['path'])
#         tg_groups = TgGroup.objects.filter(**msg)
#         if list(tg_groups) != []:
#             for tg_group in tg_groups:
#                 print(f'this message already exists in [green]tg_groups [cyan]{tg_group.message_id}')
#         else:
#             gr = TgGroup.objects.create(**msg)
#             print(f'{msg["message_id"]} saved to db group')


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


insert_or_get_execution("h:\Exports\SmartTech Learning Group",'SmartTech Learning')

#
# end_text = 'Collecting successfully end!'
# f = Figlet(font='doom')
# print(f.renderText(end_text))