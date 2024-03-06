

def slice_target_len(src,dst):
    sources = src.split('\\')
    file_name = sources[-1]

    if len(f'{dst}/{file_name}') > 259:
        minus_value = len(f'{dst}/{file_name}') - 259
        file_type = file_name.split('.')[1]
        file_name1 = file_name.split('.')[0]
        file_name = f'{file_name1[:len(file_name1) - minus_value].strip()}.{file_type}'
        return file_name
    else:
        file_name = file_name
    return file_name


