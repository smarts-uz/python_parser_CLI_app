from Check_path.check_src_path import check_path_Src
from Telegram.tg_bot import send_error_msg
import os
from retry import retry
from dotenv import load_dotenv
load_dotenv()
retry_delay = int(os.getenv('retry_delay'))
retry_tries = int(os.getenv('retry_tries'))
retry_max_delay = int(os.getenv('retry_max_delay'))
retry_jitter = int(os.getenv('retry_jitter'))

def hashtag_txt(dst_path,hashtag_name,tg_channel_id,hashtag):
    check_path_Src()
    print(f'Created # txt file path: {dst_path}')
    try:
        with open(f'{dst_path}/#{hashtag_name}.txt', 'w', encoding='utf=8') as file:
            file.write(f'#{hashtag}')
    except Exception as e:
        print(e)
        send_error_msg(error=e, group_id=tg_channel_id)