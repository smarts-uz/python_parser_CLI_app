import os.path
import time

from django_orm.db.db_functions import get_content_from_tg_channel_by_ex_id, get_data_tg_channel_nonempty, \
    change_status_execution, get_data_channel_id_none, update_target_group, update_last_copy_file_pk, \
    get_execute_name_for_nonparentmessage
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files


def copy_file(ex_id):
    i = 0
    k = 0
    n = 0
    channels = get_content_from_tg_channel_by_ex_id(ex_id=ex_id)
    change_status_execution(id=ex_id, filemove_process=True)
    for channel in channels:
        i += 1
        print(f'channel:{i}: pk:{channel.pk} ex_id:{channel.execution_id} content:{channel.text}')
        path = file_creator(actual_path1=channel.text, custom_date=channel.date,file_path=channel.file_path,main_path=channel.path)
        path = f'{path.strip()}\\'
        groups = get_data_tg_channel_nonempty(ex_id=ex_id, channel_id=channel.pk)

        for group in groups:
            update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
            update_target_group(pk=group.pk, target=path)
            k += 1
            copy_all_files(group=group, path=path)

    nonparent_data = get_data_channel_id_none(ex_id=ex_id)
    for group in nonparent_data:
        n += 1
        update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
        group_name = get_execute_name_for_nonparentmessage(ex_id=ex_id)
        path = file_creator(actual_path1=group_name,custom_date=group.date)

        copy_all_files(group=group, path=path)
        update_target_group(pk=group.pk, target=path)
    change_status_execution(id=ex_id, completed=True)
    print('Total count of Nonparent data:', n)
    print('Total count of Channel id\'s not null data:', k)


    # except Exception as e:
    #     print('Error:',e)