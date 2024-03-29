import os.path
import shutil
import time

from Telegram.tg_bot import send_error_msg
from django_orm.db.db_functions import update_last_copy_file_pk, get_execute_name_for_nonparentmessage, \
    update_target_group, get_name_from_channel, change_status_execution
from file_copy.check_create_folder import file_creator
from file_copy.copy_foreach_file.group_tg_channel_id_none import tg_channel_id_none
from file_copy.copy_foreach_file.group_tg_channel_id_not_none import tg_channel_id_not_none

from file_copy.copy_shutil import copy_all_files
import natsort

from file_copy.copy_shutil_func.copy_file_custom_date import copy_file_with_custom_date
from log3 import Logger

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')

def copy_file_for_each(groups,ex_id):
    k = 0
    i = 0
    l = 0
    for group in natsort.os_sorted(groups):
        k += 1
        match group.tg_channel_id:
            case None:
                i = tg_channel_id_none(group=group,ex_id=ex_id,i=i)
            case _:
                l = tg_channel_id_not_none(group=group,ex_id=ex_id,l=l)
    print(f"""Copied files count: {k}
                                channel id none: {i}
                                channel id not none: {l}""")
    change_status_execution(id=ex_id, completed=True)



#
#
# def copy_file_for_each(groups,ex_id):
#     k = 0
#     i = 0
#     l = 0
#     for group in natsort.os_sorted(groups):
#         k += 1
#         match group.tg_channel_id:
#             case None:
#                 update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
#                 i += 1
#                 name = get_execute_name_for_nonparentmessage(ex_id=ex_id)
#                 path = file_creator(actual_path1='____', channel_name=name,custom_date=group.date,tg_channel_id=group.pk)
#                 copy_all_files(group=group, path=path)
#                 # update_target_group(pk=group.pk, target=path)
#             case _:
#                 channel = get_name_from_channel(channel_id=group.tg_channel_id)
#                 l += 1
#                 update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
#                 name = channel[0]
#                 custom_date = channel[1]
#                 file_path = channel[3]
#                 if name == None and file_path !=None:
#                     name = file_path.split('/')[-1].split('.')[0]
#                 else:
#                     name = name
#                 try:
#                     path = file_creator(actual_path1=name.strip(), custom_date=custom_date, channel_name=channel[2],tg_channel_id=group.tg_channel_id)
#                     if file_path !=None:
#                         file_name =file_path.split('/')[-1]
#                         cp_path = path.replace(name,'')
#                         dst_path = os.path.isfile(os.path.join(cp_path,file_name))
#                         src_path= f'{channel[4]}/{file_path}'
#                         print(src_path)
#                         match dst_path:
#                             case True:
#                                 print('already copied this file')
#                             case False:
#                                 copy_file_with_custom_date(src=src_path, dst=cp_path, custom_date=custom_date,file_name=file_name)
#                                 print(f'copied file: {file_name}')
#                         time.sleep(50)
#                 except Exception as e:
#                     print(e)
#                     send_error_msg(error=e, group_id=group.pk)
#                     current.err(e)
#                     history.err(e)
#                     statistic.err(e)
#                 copy_all_files(group=group, path=path)
#                 # update_target_group(pk=group.pk, target=path)
#     print(f"""Copied files count: {k}
#                         channel id none: {i}
#                         channel id not none: {l}""")
#     change_status_execution(id=ex_id, completed=True)
