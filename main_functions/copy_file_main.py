import os.path
import time

from django_orm.db.db_functions import get_content_from_tg_channel_by_ex_id, get_data_tg_channel_nonempty, \
    change_status_execution, get_data_channel_id_none, update_target_group, update_last_copy_file_pk
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files


def copy_file(ex_id):
    i = 0
    k = 0
    channels = get_content_from_tg_channel_by_ex_id(ex_id=ex_id)
    for channel in channels:
        i += 1
        print(f'channel:{i}: pk:{channel.pk} ex_id:{channel.execution_id} content:{channel.text}')
        path = file_creator(actual_path1=channel.text)

        groups = get_data_tg_channel_nonempty(ex_id=ex_id, channel_id=channel.pk)
        print(f'tg_channels not None\'s count: {len(groups)}')
        change_status_execution(id=ex_id, filemove_process=True)
        for group in groups:
            update_target_group(pk=group.pk,target=path)
            update_last_copy_file_pk(ex_id=ex_id,id=group.pk)
            k +=1
            print(k)
            copy_all_files(group=group,path=path)
    nonparent_data = get_data_channel_id_none(ex_id=ex_id)
    for group in nonparent_data:
        path = file_creator(actual_path1='All')
        update_target_group(pk=group.pk, target=path)
        update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
        copy_all_files(group=group,path=path)


    print('Total count of group:',k)
