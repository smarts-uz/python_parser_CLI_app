import os
from datetime import datetime
def check_file_exists(src,byte):
    file = os.path.isfile(src)
    match file:
        case False:
            return False
        case True:
            byte_f = os.path.getsize(filename=src)
            if byte_f == byte:
                return True
            else:
                return False