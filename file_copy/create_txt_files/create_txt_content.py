import time

from Telegram.tg_bot import send_error_msg
from file_copy.copy_shutil_func.slice_target_content_len import slice_target_content_lens
from file_copy.silicing_long_words.slicing_words_file import slice_content_words
from rich import print
import os
from log3 import Logger

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')

def create_txt_content(content,path,txt_name,custom_date,group_id):
    txt_name = slice_content_words(text=txt_name)
    text = f""""{content}"
            """
    txt_name = slice_target_content_lens(path=path, filename=txt_name)
    if os.path.isfile(f'{path}/{txt_name}.txt'):
        print(f'This txt [purple4 bold]{path}/{txt_name}.txt file is already created!')
    else:
        try:
            with open(f'{path}/{txt_name}.txt', mode="w", encoding='utf-8') as file:
                print(f'Created txt file [green_yellow bold]{path}/{txt_name}.txt')
                file.write(text)
            os.utime(f'{path}/{txt_name}.txt', (custom_date.timestamp(), custom_date.timestamp()))
        except Exception as e:
            print(f'[red]Error {e}')
            send_error_msg(error=e, group_id=group_id)
            current.err(e)
            history.err(e)
            statistic.err(e)
