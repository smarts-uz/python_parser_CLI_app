import os

from dotenv import load_dotenv
load_dotenv()



def slice_target_len(file_name,dst):
    max_folder_len = int(os.getenv('max_folder_len'))
    max_file_len = int(os.getenv('max_file_len'))
    if len(dst) > max_folder_len:
        dst = dst[:max_folder_len]
    else:
        dst = dst
    file_len = int(max_file_len) - len(dst)
    if len(file_name) > file_len:
        file_name = file_name[:file_len]
    else:
        file_name = file_name
    return file_name,dst


