import natsort

from django_orm.db.db_functions import get_last_copied_pk, get_data_from_group, update_target_group, \
    update_last_copy_file_pk, get_name_from_channel, change_status_execution, get_execute_name_for_nonparentmessage
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files
from main_functions.copy_file_main import copy_file


def file_copy_pr(ex_id):
    last_pk = get_last_copied_pk(ex_id=ex_id)
    match last_pk:
        case None:
            print(f'Last copied file returned None. Copy process starts at the begin!')
            copy_file(ex_id)
        case _:
            print(f'Last copied file is :{last_pk}')
            groups = get_data_from_group(ex_id=ex_id, last_id=last_pk - 1)
            print(f'File copy process count: {len(groups)}')
            k = 0
            i = 0
            l = 0
            for group in natsort.os_sorted(groups):
                k += 1
                match group.tg_channel_id:
                    case None:
                        update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
                        i += 1
                        name = get_execute_name_for_nonparentmessage(ex_id=ex_id)
                        path = file_creator(actual_path1='____', channel_name=name)
                        copy_all_files(group=group, path=path)
                        update_target_group(pk=group.pk, target=path)
                    case _:
                        channel = get_name_from_channel(channel_id=group.tg_channel_id)
                        l += 1
                        update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
                        name = channel[0]
                        custom_date = channel[1]
                        path = file_creator(actual_path1=name.strip(), custom_date=custom_date, channel_name=channel[2])
                        copy_all_files(group=group, path=path)
                        update_target_group(pk=group.pk, target=path)
            print(f"""Copied files count: {k}
                    channel id none: {i}
                    channel id not none: {l}""")
            change_status_execution(id=ex_id, completed=True)


    # except Exception as e:
    #     print(e)


