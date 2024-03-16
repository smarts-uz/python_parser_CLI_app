import time

from rich import print
import os
from Telegram.tg_bot import send_error_msg
from django_orm.db.db_functions import get_file_paths, update_target_group
from file_copy.check_file_exists import check_file_exists
from file_copy.copy_shutil_func.copy_file_custom_date import copy_file_with_custom_date
from file_copy.copy_shutil_func.slice_target_lenth import slice_target_len
from file_copy.file_copy_functions import remove_unsupported_chars, create_txt_file_content
from file_copy.http.find_https_link import find_https, create_url_file
from file_copy.increment_file_name.increment import get_incremented_filename
from file_copy.remove_unsupported_chars.replace_backslash_to_slash import replace_backslash
from log3 import Logger

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')
def false_absent(group,path):
    file = get_file_paths(pk=group.pk)
    file_path = file[0]
    file_name_ex = file[1]
    file_name = file[2]
    type = file[3]
    match group.content:
        case None:
            slicing = slice_target_len(file_name=file_name, dst=path)
            file_name = slicing[0]
            path = slicing[1]
            file_name_ex = f'{file_name}.{type}'
            print(
                f'[bright_green]{group.pk}\'s File {group.file_path.split('/')[1]} copy process starting Size: [green bold]{group.size} Duration: [green bold]{group.duration}')
            check = check_file_exists(src=os.path.join(path, file_name_ex), byte=group.byte)
            if check == True:
                print(f'This [purple4]{group.pk}\'s File {group.file_path.split('/')[1]} is  already copied')
                match group.target:
                    case None:
                        update_target_group(pk=group.pk, target=os.path.join(path, file_name_ex))
            else:
                file_name_ex_1 = get_incremented_filename(filename=os.path.join(path, file_name_ex))
                file_name_ex_1 = replace_backslash(text=file_name_ex_1).split('/')[-1]
                copy_file_with_custom_date(src=file_path, dst=path, custom_date=group.date, group_id=group.pk,
                                           file_name=file_name_ex_1)
        case _:
            if type !='mhtml' and type !='url':
                content = remove_unsupported_chars(text=group.content, hashtag=True)[0]
                slicing = slice_target_len(file_name=content, dst=path)
                file_name_new = slicing[0]
                path = slicing[1]
                file_name_ex = f'{file_name_new}.{type}'
                destination_file_path = os.path.join(path, file_name_ex)
            else:
                slicing = slice_target_len(file_name=file_name_ex, dst=path)
                file_name_ex = slicing[0]
                path = slicing[0]
                destination_file_path = os.path.join(path, file_name_ex)
            check = check_file_exists(src=destination_file_path, byte=group.byte)
            if check == True:
                print(f'This [purple4]{group.pk}\'s data is  already copied')
                match group.target:
                    case None:
                        update_target_group(pk=group.pk, target=destination_file_path)
            else:
                print(
                    f'[bright_green]{group.pk}\'s File [green bold]{group.file_path.split('/')[1]} [bold]copy process starting Size: [green bold]{group.size} Duration: [green bold]{group.duration} Content: [green bold]{group.content}')
                dst = copy_file_with_custom_date(src=file_path, dst=path, custom_date=group.date,
                                                 group_id=group.pk, file_name=file_name_ex)
                if os.path.join(path, file_name_ex) != destination_file_path:
                    try:
                        destination_file_path = get_incremented_filename(filename=destination_file_path)
                        if type == 'mhtml' or type == 'url':
                            pass
                        else:
                            os.rename(src=dst, dst=destination_file_path)
                            print(f'[orchid1]{group.pk} file renamed {destination_file_path.split('\\')[-1]}')
                    except Exception as e:
                        print(e)
                        send_error_msg(error=e, group_id=group.pk)
                        current.err(e)
                        history.err(e)
                        statistic.err(e)
                if type == 'mhtml' or type == 'url':
                    pass
                else:
                    create_txt_file_content(content=group.content, path=path,
                                            txt_name=f'{file_name}.{type}', custom_date=group.date, group_id=group.pk)
