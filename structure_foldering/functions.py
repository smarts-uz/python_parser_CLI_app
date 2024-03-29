import os
from os import listdir
from log3 import Logger


def correct_post_title(post_title):
    first_step = post_title.split('|')
    first_step_2 = []
    if len(first_step) != 1:
        for i in first_step:
            var = i.strip()
            first_step_2.append(var)
        second_step = first_step_2[-1].split('#')
        third_step = second_step[0]
        first_step_2[-1] = third_step
        first_step_2.reverse()
        # for k in first_step_2:
        #     index = first_step_2.index(k)
        #     if len(k.split('https:')) > 2:
        #         temp = k.split('https:')
        #         variable = [temp[0]]
        #     elif len(k.split('/')) > 2:
        #         variable = k.split('/')
        #     elif len(k.split('\\')) > 2:
        #         variable = k.split('\\')
        #     elif len(k.split(':')) > 2:
        #         variable = k.split(':')
        #     else:
        #         variable = k
            # try:
            #     if len(variable) > 1:
            #         variable.reverse()
            #         first_step_2.pop(index)
            #         for y in variable:
            #             first_step_2.insert(index, y)
            #     else:
            #         first_step_2.pop(index)
            #         first_step_2.insert(index, variable[0])
            # except Exception as e:
            #     print(e)
        return first_step_2
    else:
        second_step = first_step[-1].split('#')
        third_step = second_step[0]
        first_step[-1] = third_step
        first_step.reverse()
        return first_step


def correct_video_title(video_path, post_title):
    first_step = video_path.split('video_files')
    if first_step[-1].startswith('/Rec'):
        video_title = '\\' + post_title[-1] + '.mp4'
    else:
        video_title_1 = first_step[-1]
        first_step = video_title_1.split('/')
        video_title = '\\' + first_step[-1]
    return video_title


def correct_data_title(data_title):
    formatted_date = data_title.strftime("%Y-%m-%d %H:%M:%S")
    year = formatted_date[0:4]
    return year


def correct_file_location(video_path, data_title, base_dir):
    # base_dir = "E:\SmartTech Learning Group\\"
    file_directory = base_dir + data_title
    file_path_list = listdir(file_directory)
    for i in file_path_list:
        link = file_directory + '\\' + i
        video_link = link + '\\' + video_path
        if os.path.isfile(video_link):
            return video_link


def correct_video_duration(video_duration):
    result = '-'.join(video_duration.split(':'))
    return result


# https://www.youtube.com/watch?v=1Q6pw9gPDp0
# https://stackoverflow.com/questions/41116013/selenium-code-to-scroll-horizontally-in-a-web-element-which-is-loading-lazily
# https://koofr.eu/
def correct_url_name(url):
    first_step = url.split('https://')
    second_step = first_step[1].split('/')
    last_step = second_step[-1]
    if last_step == '':
        if len(second_step[-2]) < 100:
            return second_step[-2]
        else:
            return second_step[-2][:30]
    else:
        if len(last_step) < 100:
            return last_step
        else:
            return last_step[:30]


def create_link(actual_path, url_name, content):
    statistic = Logger('statictics', 'a')
    with open(f'{actual_path}{url_name}.url', 'x', encoding='UTF-8') as file:
        a='000214A0-0000-0000-C000-000000000046'
        str = f"""
[{a}]
Prop3=19,11
[InternetShortcut]
IDList=
URL='''+{content}+'''
IconIndex=13
HotKey=0
IconFile=C:\\Windows\\System32\\SHELL32.dll"""

        statistic.log(str)
        print(f'[green]!{str}')

        file.write(str)


def create_video_note(actual_path, video_title, description, video_duration, from_name):
    if description is None:
        description = 'None'
    with open(f'{actual_path}{video_title}.tmnote', 'x', encoding='UTF-8') as file:
        file.write(f'''Description: {description}
Video_duration: {video_duration}
From_name: {from_name}''')


def create_folder_to_save(path_to_save, main_folder_name):
    if not os.path.exists(path_to_save + main_folder_name):
        os.mkdir(path_to_save + main_folder_name)
    path = path_to_save + main_folder_name + '\\'
    return path



#  \\192.168.100.100\SmartTech Learning Group\2023\9-8\video_files\«Account» folder of Services.mp4 True
#  \\192.168.100.100\SmartTech Learning Group\\2023\9-8\video_files\«Account» folder of Services.mp4  false

# "\\192.168.1.236\Exports\SmartTech Learning Group\2023\8-18\files\Name Everything _ Introduction to DhiWise - DhiWise.mhtml" True
# '\\192.168.1.236\Exports\SmartTech Learning Group\2023\8-18\files/Name Everything _ Introduction to DhiWise - DhiWise.mhtml' False
