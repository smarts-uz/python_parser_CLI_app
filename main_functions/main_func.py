import os

from file_copy.check_create_folder import file_creator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import *
from pprint import pprint

from log3 import Logger
current_l = Logger('current', 'w')
from django_orm.db.db_functions import get_path_by_execution_id, get_all_none_channel_id_from_group, get_channel_id, \
    change_status_execution, update_channel_id, get_execution_data_from_id, get_content_from_tg_channel_by_ex_id, \
    get_data_tg_channel_nonempty
from django_orm.db.db_save import insert_data_to_db
from parsing.foreach_parser import parsing_foreach
from main_functions.process_cmdline import cmd_process
from main_functions.run import run_parsing


def main_execute(ex_id):
    execution = get_execution_data_from_id(ex_id=ex_id)
    match execution.status:
        case 'completed':
            pass
        case 'parsing_process' | 'new' if cmd_process() != None and f'--ex_id={execution.pk}' in cmd_process():
            print(cmd_process())
            print(f'This execution {execution.pk} is already running please wait until end!!!')
        case 'parsing_process' | 'new' if cmd_process() != None and f'--ex_id={execution.pk}' not in cmd_process():
            print(f'parsing is starting ex_id: {execution.pk}')
            pars = run_parsing(execution.pk)
            match pars:
                case 0:
                    print(f'Current execution[{execution.pk}] is ready to copy')
                case _:
                    print('Warning problem')
        case 'tg_channel_empty':
            print('tg_channel_empty')
            # main_empty_channel()
        case 'parsing_ok':
            print(f'Ready to copy to folder {execution.pk}')









# def main_execute(exe):
#     if exe['status'] == 'parsing_process' or exe['status'] == 'new':
#         get_proces = cmd_process()
#         print(exe)
#         if get_proces !=None:
#             if f'--ex_id={exe['pk']}' in get_proces:
#                 print(get_proces)
#                 print(f'This execution {exe['pk']} is already running please wait until end!!!')
#             else:
#                 print(f'parsing is starting ex_id: {exe['pk']}')
#                 pars = run_parsing(exe['pk'])
#                 if pars == 0:
#                    print('ok no problem')
#                 else:
#                     print('warning! problem')
#         else:
#             print(f'parsing is starting ex_id: {exe['pk']}')
#             pars = run_parsing(exe['pk'])
#             if pars == 0:
#                 print('ok')
#             else:
#                 print('warning! problem')




def main_parsing(ex_id):
    try:
        path = get_path_by_execution_id(ex_id)[1]
        channel_name = get_path_by_execution_id(ex_id)[0]
        current = get_path_by_execution_id(ex_id)[2]
        parsing_data = parsing_foreach(path=path,execution_id=ex_id,channel_name=channel_name,current_html=current)
        save_info = insert_data_to_db(parsing_data)
        channel_count = save_info[0]
        group_count = save_info[1]
        print(f'[green]Success')
        print(f'[cyan]Channel: [blue]exist:{channel_count[0]}, [green]new:{channel_count[1]}')
        print(f'[cyan]Group: [blue]exist:{group_count[0]}, [green]new:{group_count[1]}')
    except Exception as e:
        current_l.log(e)
        print(e)

def main_empty_channel():
    found = 0
    notfound = 0
    empties = get_all_none_channel_id_from_group()
    print(f'Channel id\'s None count : {len(empties)}')
    for empty in empties:
        channel_id = get_channel_id(msg_id=empty['replied_message_id'],channel_name=empty['channel_name'])
        update_channel_id(pk=empty['pk'],channel_id=channel_id)
        if channel_id != None:
            found+=1
            print(f'id = {empty['pk']}\'s channel_id updated = {channel_id} ')
        else:
            notfound+=1
            print(f' {empty['pk']} Channel id not found')
        change_status_execution(id=empty['execution_id'], parsing_ok=True)
    print(f'Channel id found: {found}')
    print(f'Channel id not found: {notfound}')


def copy_file(ex_id):
    i = 0
    channels = get_content_from_tg_channel_by_ex_id(ex_id=ex_id)
    for channel in channels:
        i += 1
        print(f'channel:{i}: pk:{channel.pk} ex_id:{channel.execution_id} content:{channel.text}')
        path = file_creator(actual_path1=channel.text)
        groups = get_data_tg_channel_nonempty(ex_id=ex_id, channel_id=channel.pk)
        k = 0
        print()
        for group in groups:
            pass
            # k += 1
            # print(
            #     f'group:{k}: pk:{group.pk} channel_id:{group.tg_channel_id},ex_id:{group.execution_id} content:{group.content} files:{group.file_path}')
        print()


