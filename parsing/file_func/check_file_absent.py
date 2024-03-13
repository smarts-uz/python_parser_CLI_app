import os
def check_file_absent(path,file_path):
    file_path = file_path.replace('\\','/')
    f_path = f'{path}/{file_path}'
    isFile = os.path.isfile(f_path)
    byte = None
    if isFile == True:
        byte = os.path.getsize(filename=f_path)
        return False,byte
    else:
        return True,byte