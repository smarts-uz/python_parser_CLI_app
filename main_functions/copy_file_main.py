import os
import shutil

from django_orm.db.db_functions import get_content_from_tg_channel_by_ex_id, get_data_tg_channel_nonempty, \
    change_status_execution, get_file_paths
from file_copy.check_create_folder import file_creator
from file_copy.file_copy_functions import  remove_unsupported_chars, create_txt_file_content

def copy_file(ex_id):
    i = 0
    k = 0
    channels = get_content_from_tg_channel_by_ex_id(ex_id=ex_id)
    for channel in channels:
        i += 1
        print(f'channel:{i}: pk:{channel.pk} ex_id:{channel.execution_id} content:{channel.text}')
        path = file_creator(actual_path1=channel.text)
        groups = get_data_tg_channel_nonempty(ex_id=ex_id, channel_id=channel.pk)
        print(f'tg_channels not None\' count: {len(groups)}')
        change_status_execution(id=ex_id, filemove_process=True)
        for group in groups:
            k += 1
            print(k)
            match group.absent:
                case False:
                    print('file_copy',group.pk)
                    file = get_file_paths(pk=group.pk)
                    file_path = file[0]
                    file_name_ex = file[1]
                    file_name = file[2]
                    type = file[3]
                    match group.content:
                        case None:
                            print('file_copy without content', group.pk)
                            shutil.copy(file_path, path)
                        case _:
                            print('file_copy with content', group.pk)
                            content = remove_unsupported_chars(text=group.content)
                            destination_file_path = os.path.join(path,f'{content}.{type}')
                            print(destination_file_path)
                            if os.path.isfile(destination_file_path):
                                print('This file is already copied')
                            else:
                                try:
                                    shutil.copy2(file_path, path)
                                    os.rename(os.path.join(path, file_name_ex), destination_file_path)
                                    create_txt = create_txt_file_content(content=group.content, path=path,
                                                                         txt_name=f'{content}.{type}')
                                except:
                                    continue


                case True:
                    print('message txt', group.pk)
                    print(group.content,group.pk,group.message_id)
                    content = remove_unsupported_chars(text=group.content)
                    create_txt = create_txt_file_content(content=group.content, path=path, txt_name=f'{content}')

    print('Total count of group:',k)

#
# a = get_content_from_tg_channel_by_ex_id(ex_id=261)
# print(a)
# for i in a:
#     print(i.pk)