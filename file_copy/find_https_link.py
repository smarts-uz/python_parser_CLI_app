import os.path
import re

def find_https(content):
    pattern = r'http\S+'
    reg = re.findall(pattern,content.lower())
    return reg




def create_url_file(url,name,path,custom_date):
    file_url = os.path.isfile(f'{path}\\{name}.url')
    match file_url:
        case True:
            print(f'This url {path}\\{name}.url already created')
        case False:
            with open(f'{path}\\{name}.url', 'w', encoding='UTF-8') as file:
                a = '{000214A0-0000-0000-C000-000000000046}'
                str = f"""[{a}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=\n{url}
IconIndex=13
HotKey=0
IconFile=C:\\Windows\\System32\\SHELL32.dll"""
                file.write(str)
            os.utime(f'{path}\\{name}.url', (custom_date.timestamp(), custom_date.timestamp()))



