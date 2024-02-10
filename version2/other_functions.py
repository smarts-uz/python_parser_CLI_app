def file_choose(photo_url,ogg_url,video_url,file_url):
    if photo_url != None:
        file_path = photo_url
    elif ogg_url != None:
        file_path = ogg_url
    elif video_url != None:
        file_path = video_url
    elif file_url != None:
        file_path = file_url
    else:
        file_path = None
    return file_path

def choose_duration(duration_ogg,duration_video):
    if duration_ogg != None:
        duration = duration_ogg
    elif duration_video != None:
        duration = duration_video
    else:
        duration = None
    return duration

def folder_path(path):
    f_path = path.split('\\')
    f_path.pop()
    return '\\'.join(f_path)