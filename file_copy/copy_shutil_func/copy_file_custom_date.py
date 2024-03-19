import os
import shutil

from Check_path.check_src_path import check_path_Src
from Telegram.tg_bot import send_error_msg
from django_orm.db.db_functions import update_target_group
from log3 import Logger

current = Logger('current', 'a')
from rich import print
from retry import retry
from dotenv import load_dotenv
load_dotenv()
retry_delay = int(os.getenv('retry_delay'))
retry_tries = int(os.getenv('retry_tries'))
retry_max_delay = int(os.getenv('retry_max_delay'))
retry_jitter = int(os.getenv('retry_jitter'))

def copy_file_with_custom_date(src, dst, custom_date,file_name,group_id=None):
    global file_dst
    check_path_Src()
    try:
        file_dst = shutil.copy(src=src, dst=f'{dst}/{file_name}')
        print('[cyan]File copied successfully')
        if group_id !=None:
            update_target_group(pk=group_id, target=file_dst)
    # Set the custom date
        os.utime(file_dst, (custom_date.timestamp(), custom_date.timestamp()))
        return file_dst
    except Exception as e:
        print(e)
        send_error_msg(error=e,group_id=group_id)
        current.err(e)
