import os


from natsort import os_sorted

from parsing.functions import correct_time_data

def html_search(path):
    html_files = []
    if '\\messages.html' in path:path = path[:-len('\\messages.html')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('message') and file.endswith('.html'):
                file_m = os.path.join(root, file)
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return os_sorted(html_files)
2



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


def search_message_html(path):
    html_files = []
    if '\\messages.html' in path:path = path[:-len('\\messages.html')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('message') and file.endswith('s.html'):
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return os_sorted(html_files)


def current_html_name(html_name):
    current = html_name.split('\\')
    return current[-1]



def clear_fix_message(main_message,execution_id,path):
    msg_details = main_message['id']
    msg_id = main_message['id'][7:]
    message_body = main_message.find('div', class_='body')
    original_date = message_body.find('div', class_='pull_right date details')['title']
    date = correct_time_data(original_date)
    from_name = message_body.find('div', class_='from_name').get_text(strip=True)

    try:
        text = message_body.find('div', class_='text').get_text(strip=True)
    except:
        text = message_body.find('div', class_='text')
    try:
        media = message_body.find('div', class_='media_wrap clearfix')
        try:
            photo_url = media.find('a', class_='photo_wrap clearfix pull_left')['href']
        except:
            photo_url = None

        try:
            ogg_url = media.find('a', class_='media clearfix pull_left block_link media_voice_message')['href']
            duration_ogg = media.find('a',
                                      class_='media clearfix pull_left block_link media_voice_message').find(
                'div', class_='status details').get_text(strip=True)

        except:
            ogg_url = None
            duration_ogg = None

        try:
            video = media.find('a', class_='video_file_wrap clearfix pull_left')
            video_url = media.find('a', class_='video_file_wrap clearfix pull_left')['href']
            duration_video = video.find('div', class_='video_duration').get_text(strip=True)
        except:
            video_url = None
            duration_video = None

        try:
            file = media.find('a', class_='media clearfix pull_left block_link media_file')
            file_url = media.find('a', class_='media clearfix pull_left block_link media_file')['href']
            size = file.find('div', class_='status details').get_text(strip=True)
        except:
            file_url = None
            size = None

    except:
        media = None
        file_url = None

        size = None

    file_path = file_choose(photo_url, ogg_url, video_url, file_url)
    duration = choose_duration(duration_ogg, duration_video)

    try:
        reply_to_details = message_body.find('div', class_='reply_to details').find('a')['href']
        reply_to_message_id = message_body.find('div', class_='reply_to details').find('a')['href'][14:]

    except:
        reply_to_details = None
        reply_to_message_id = None

    if msg_id != None:
        msg_id = f'{execution_id}{msg_id}'

    if reply_to_message_id != None:
        reply_to_message_id = f'{execution_id}{reply_to_message_id}'
    return {
        "message_id": msg_id,
        "message_details": msg_details,
        "text": text,
        "file_path": file_path,
        "duration": duration,
        "size": size,
        'reply_to_msg_id': reply_to_message_id,
        "replied_message_details": reply_to_details,
        'date': date,
        'from_name': from_name,
    }


def joined_msg(joined_message,execution_id,path):
    msg_details = joined_message['id']

    msg_id = joined_message['id'][7:]
    message_body = joined_message.find('div', class_='body')
    original_date = message_body.find('div', class_='pull_right date details')['title']
    date = correct_time_data(original_date)

    try:
        reply_to_details = message_body.find('div', class_='reply_to details').find('a')['href']
        reply_to_message_id = reply_to_details[14:]

    except:
        reply_to_details = None
        reply_to_message_id = None

    try:
        text = message_body.find('div', class_='text').get_text(strip=True)
    except:
        text = message_body.find('div', class_='text')
    try:
        media = message_body.find('div', class_='media_wrap clearfix')
        try:
            photo_url = media.find('a', class_='photo_wrap clearfix pull_left')['href']
        except:
            photo_url = None

        try:
            ogg_url = media.find('a', class_='media clearfix pull_left block_link media_voice_message')['href']
            duration_ogg = media.find('a',
                                      class_='media clearfix pull_left block_link media_voice_message').find(
                'div', class_='status details').get_text(strip=True)

        except:
            ogg_url = None
            duration_ogg = None
        try:
            video = media.find('a', class_='video_file_wrap clearfix pull_left')
            video_url = media.find('a', class_='video_file_wrap clearfix pull_left')['href']
            duration_video = video.find('div', class_='video_duration').get_text(strip=True)
        except:
            video_url = None
            duration_video = None

        try:
            file = media.find('a', class_='media clearfix pull_left block_link media_file')
            file_url = media.find('a', class_='media clearfix pull_left block_link media_file')['href']
            size = file.find('div', class_='status details').get_text(strip=True)
        except:
            file_url = None
            size = None

    except:
        media = None
        file_url = None
        duration = None
        size = None

    file_path = file_choose(photo_url, ogg_url, video_url, file_url)
    duration = choose_duration(duration_ogg, duration_video)

    if msg_id != None:
        msg_id = f'{execution_id}{msg_id}'
    if reply_to_message_id != None:
        reply_to_message_id = f'{execution_id}{reply_to_message_id}'

    return {
        'message_id': msg_id,
        'message_details': msg_details,
        'date': date,
        "replied_message_id": reply_to_message_id,
        'replied_message_details': reply_to_details,
        "content": text,
        "file_path": file_path,
        "duration": duration,
        "size": size,
    }


