from django_orm.db.db_functions import change_status_execution, get_data_from_group_copy_file
import natsort

from file_copy.copy_file_foreach import copy_file_for_each


def copy_file(ex_id):
    groups = get_data_from_group_copy_file(ex_id=ex_id)
    change_status_execution(id=ex_id, filemove_process=True)
    print(f'File copy process count: {len(groups)}')
    groups = natsort.os_sorted(groups)
    copy_file_for_each(groups,ex_id=ex_id)




# def copy_file(ex_id):
#     i = 0
#     k = 0
#     n = 0
#     channels = get_content_from_tg_channel_by_ex_id(ex_id=ex_id)
#     change_status_execution(id=ex_id, filemove_process=True)
#     for channel in channels:
#         i += 1
#         print(f'channel:{i}: pk:{channel.pk} ex_id:{channel.execution_id} content:{channel.text}')
#         if channel.text != None:
#             path = file_creator(actual_path1=channel.text,channel_name=channel.from_name, custom_date=channel.date,file_path=channel.file_path,main_path=channel.path)
#         else:
#             channel_text = channel.file_path.split('/')[1]
#             path = file_creator(actual_path1=channel_text, custom_date=channel.date,file_path=channel.file_path,main_path=channel.path)
#         groups = get_data_tg_channel_nonempty(ex_id=ex_id, channel_id=channel.pk)
#
#         for group in groups:
#             update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
#             update_target_group(pk=group.pk, target=path)
#             k += 1
#             copy_all_files(group=group, path=path)
#
#     nonparent_data = get_data_channel_id_none(ex_id=ex_id)
#     for group in nonparent_data:
#         n += 1
#         update_last_copy_file_pk(ex_id=ex_id, id=group.pk)
#         group_name = get_execute_name_for_nonparentmessage(ex_id=ex_id)
#         path = file_creator(actual_path1='____',custom_date=group.date,channel_name=group_name)
#         copy_all_files(group=group, path=path)
#         update_target_group(pk=group.pk, target=path)
#     change_status_execution(id=ex_id, completed=True)
#     print('Total count of Nonparent data:', n)
#     print('Total count of Channel id\'s not null data:', k)


    # except Exception as e:
    #     print('Error:',e)