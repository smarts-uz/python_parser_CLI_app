from django_orm.db.db_functions import update_last_copy_file_pk, get_execute_name_for_nonparentmessage, \
    update_target_group, get_name_from_channel, change_status_execution
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files
import natsort

def copy_file_for_each(groups,ex_id):
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
