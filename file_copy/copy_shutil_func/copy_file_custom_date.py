import os
import shutil

from Telegram.tg_bot import send_error_msg
from django_orm.db.db_functions import update_target_group
from log3 import Logger

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')




def copy_file_with_custom_date(src, dst, custom_date,file_name,group_id=None):
    global file_dst
    try:
        file_dst = shutil.copy(src=src, dst=f'{dst}/{file_name}')
        if group_id !=None:
            update_target_group(pk=group_id, target=file_dst)

    # Set the custom date
        os.utime(file_dst, (custom_date.timestamp(), custom_date.timestamp()))
        return file_dst
    except Exception as e:
        print(e)
        send_error_msg(error=e,group_id=group_id)
        current.err(e)
        history.err(e)
        statistic.err(e)