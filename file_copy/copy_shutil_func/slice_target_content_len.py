

def slice_target_content_lens(path,filename):
    if len(f'{path}/{filename}') > 2:
        filename = filename[:len(f'{path}/{filename}')-259]
    else:
        filename =filename
    return filename