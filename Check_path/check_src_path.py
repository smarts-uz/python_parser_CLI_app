from retry import retry
from dotenv import load_dotenv
load_dotenv()
import os
retry_delay = int(os.getenv('retry_delay'))
retry_tries = int(os.getenv('retry_tries'))
retry_max_delay = int(os.getenv('retry_max_delay'))
retry_jitter = int(os.getenv('retry_jitter'))
retry_path_src = os.getenv('retry_path_src')
retry_path_dst = os.getenv('retry_path_dst')
# FileNotFoundError
@retry((FileNotFoundError,IOError), delay=retry_delay, backoff=2, max_delay=retry_max_delay, tries=retry_tries,jitter=retry_jitter)
def check_path_Src():
    print('Checking server')
    txt_name = '1q2w3e4r5t6y7u8i9o1p0w3k2d1ma32asd1.txt'
    dst_path = f'{retry_path_dst}/{txt_name}'
    with open(retry_path_src,mode='rb') as f:
        pass
    with open(dst_path,mode='w') as f:
        pass
    os.remove(dst_path)
    print('Server is okay')



