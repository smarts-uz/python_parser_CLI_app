import os


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
                print(f"find html file: {os.path.join(root, file)}")
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return html_files


def current_html_name(html_name):
    current = html_name.split('\\')
    return current[-1]


# fname_list = search_html(path)
#     channel_content_list = []
#     group_content_list = []
#
#     for folder in fname_list:
#         f_path = folder_path(folder)
#         parsing = Pars(folder)
#         main_folder_name = parsing.parsing()[2]
#         ready_information = parsing.joined_messages()
#         channel_content = parsing.main_msg()
#         channel_content_list.append(channel_content)
#         group_content_list.append(ready_information)
#
#         save_to_execution(name=main_folder_name, path=f_path, status='in_process')