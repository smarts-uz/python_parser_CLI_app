import os.path
import re
from rich import print
from Telegram.tg_bot import send_error_msg
from file_copy.copy_shutil_func.slice_target_content_len import slice_target_content_lens
from file_copy.correct_name_url_file import correct_url_name
from file_copy.file_copy_functions import remove_unsupported_chars
from file_copy.silicing_long_words.slicing_word_url import slicing_long_word_url
from log3 import Logger

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')


def find_https(content):
    pattern = r'[hH][tT]{2}[pP]\S+'
    reg = re.findall(pattern,content)
    return reg



def create_url_file(url,path,custom_date,group_id):

    name_1 = correct_url_name(url=url)
    name_1 = remove_unsupported_chars(name_1)[0]
    name_1 = slicing_long_word_url(text=name_1)
    name_1 = slice_target_content_lens(path=path,filename=name_1)
    file_url = os.path.isfile(f'{path}/{name_1}.url')
    match file_url:
        case True:
            print(f'This url [purple4 bold]{path}/{name_1}.url already created')
        case False:
            try:
                with open(f'{path.strip()}/{name_1}.url', 'w', encoding='UTF-8') as file:
                    a = '{000214A0-0000-0000-C000-000000000046}'
                    str = f"""[{a}]
Prop3=19,11
[InternetShortcut]
IDList=
URL={url}
IconIndex=13
HotKey=0
IconFile=C:\\Windows\\System32\\SHELL32.dll"""
                    file.write(str)
                if custom_date != None:
                    os.utime(f'{path}/{name_1}.url', (custom_date.timestamp(), custom_date.timestamp()))
            except Exception as e:
                print(f'[red]Error {e}')
                send_error_msg(error=e,group_id=group_id)
                current.err(e)
                history.err(e)
                statistic.err(e)




