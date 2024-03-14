from django_orm.db.db_functions import update_last_copy_file_pk, get_execute_name_for_nonparentmessage
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files


def tg_channel_id_none(group,ex_id,i):
    update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
    i += 1
    name = get_execute_name_for_nonparentmessage(ex_id=ex_id)
    path = file_creator(actual_path1='____', channel_name=name, custom_date=group.date, tg_channel_id=group.pk)
    copy_all_files(group=group, path=path)
    return i