import os
from datetime import datetime
def check_file_exists(src,mtime):
    file = os.path.isfile(src)
    match file:
        case False:
            return False
        case True:
            time = os.path.getmtime(src)
            time = datetime.fromtimestamp(time)
            if time == mtime:
                return True
            else:
                return False