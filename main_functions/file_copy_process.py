from django_orm.db.db_functions import get_last_copied_pk, get_data_from_group, update_target_group, \
    update_last_copy_file_pk, get_name_from_channel, change_status_execution
from file_copy.check_create_folder import file_creator
from file_copy.copy_shutil import copy_all_files


def file_copy_pr(ex_id):
    try:
        last_pk = get_last_copied_pk(ex_id=ex_id)
        print(f'Last copied file is :{last_pk}')
        groups = get_data_from_group(ex_id=ex_id, last_id=last_pk)
        print(f'File copy process count: {len(groups)}')
        k = 0
        i = 0
        l = 0
        for group in groups:
            k += 1
            match group.tg_channel_id:
                case None:
                    i += 1
                    path = file_creator(actual_path1='All')
                    update_target_group(pk=group.pk, target=path)
                    update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
                    copy_all_files(group=group, path=path)
                case _:
                    l += 1
                    name = get_name_from_channel(channel_id=group.tg_channel_id)
                    path = file_creator(actual_path1=name)
                    update_target_group(pk=group.pk, target=path)
                    update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
                    copy_all_files(group=group, path=path)
        print(f"""Copied files count: {k}
        channel id none: {i}
        channel id not none: {l}""")
        change_status_execution(id=ex_id, completed=True)
    except Exception as e:
        print(e)


