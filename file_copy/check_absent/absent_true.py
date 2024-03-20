
from rich import print
import os
from Telegram.tg_bot import send_error_msg
from django_orm.db.db_functions import get_file_paths, update_target_group
from file_copy.check_file_exists import check_file_exists
from file_copy.copy_shutil_func.copy_file_custom_date import copy_file_with_custom_date
from file_copy.copy_shutil_func.slice_target_lenth import slice_target_len
from file_copy.create_txt_files.create_txt_content import create_txt_content
from file_copy.file_copy_functions import remove_unsupported_chars, create_txt_file_content
from file_copy.http.find_https_link import find_https, create_url_file
from file_copy.increment_file_name.increment import get_incremented_filename
from file_copy.remove_unsupported_chars.replace_backslash_to_slash import replace_backslash
from log3 import Logger
from file_copy.copy_shutil_func.slice_target_lenth import slice_target_len


def true_absent(group,path):
    match group.content:
        case None:
            if group.file_path != None:
                print(f'[red]This file not exists [bright_green]tg_group_id:{group.pk}  [red bold]{group.file_path}')
        case _:
            content = remove_unsupported_chars(text=group.content)[0]
            slicing = slice_target_len(file_name=f'{content}', dst=path)
            file_name = slicing[0]
            path = slicing[1]
            https = find_https(group.content)
            match https:
                case []:
                    create_txt_content(content=group.content, path=path, txt_name=file_name,
                                            custom_date=group.date, group_id=group.pk)
                    # create_txt_file_content(content=group.content, path=path, txt_name=content,
                    #                         custom_date=group.date, group_id=group.pk)
                    print(f'[bright_green]{group.pk}\'s data message copied with name {content}')
                case _:

                    for http in https:
                        create_url_file(url=http, path=path, custom_date=group.date, group_id=group.pk)
                        print(f'[blue]{group.pk}\'s created [dark blue]url file {http}')
                    if len(https) > 1:
                        create_txt_file_content(content=group.content, path=path, txt_name=f'{content}',
                                                custom_date=group.date, group_id=group.pk,destination_file_path=file_name)
    update_target_group(pk=group.pk, target=path)