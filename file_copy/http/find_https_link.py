import os.path
import re
import time
from rich   import print
from file_copy.correct_name_url_file import correct_url_name
from file_copy.file_copy_functions import remove_unsupported_chars, slice_long_words, slice_words


def find_https(content):
    pattern = r'[hH][tT]{2}[pP]\S+'
    reg = re.findall(pattern,content)
    return reg




def create_url_file(url,path,custom_date):

    name_1 = correct_url_name(url=url)
    name_1 = remove_unsupported_chars(name_1)[0]
    name_1 = slice_words(text=name_1)

    file_url = os.path.isfile(f'{path}\\{name_1}.url')
    match file_url:
        case True:
            print(f'This url [blue bold]{path}\\{name_1}.url already created')
        case False:
            with open(f'{path.strip()}\\{name_1}.url', 'w', encoding='UTF-8') as file:
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
                os.utime(f'{path}\\{name_1}.url', (custom_date.timestamp(), custom_date.timestamp()))




