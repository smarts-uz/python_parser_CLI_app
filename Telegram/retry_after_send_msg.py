

import re
import time
def retry_after(text):
    text = str(text)
    result = re.search("retry after", text)
    if result:
        # matching = re.findall(r'\b\d+\.\d+\b', str) for float
        matching = re.findall(r'\b\d+\b', text)   #for integer
        num = int(matching[1].split('.')[0])
        for i in range(1,num+1):
            time.sleep(1)
            print(f"retry after : {i}")
        # print('success')
        time.sleep(1)