import shutil
import os

from django_orm.db.db_functions import get_file_paths
from file_copy.file_copy_functions import remove_unsupported_chars, create_txt_file_content


def copy_file(path,file):
    shutil.copy2(file, path)



def copy_all_files(group,path):

    match group.absent:
        case False:
            print('file_copy', group.pk)
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
                    destination_file_path = os.path.join(path, f'{content}.{type}')
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
                           pass

        case True:
            print('message txt', group.pk)
            print(group.content, group.pk, group.message_id)
            content = remove_unsupported_chars(text=group.content)
            create_txt = create_txt_file_content(content=group.content, path=path, txt_name=f'{content}')

