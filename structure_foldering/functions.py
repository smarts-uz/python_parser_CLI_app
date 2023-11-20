import os
from os import listdir
import datetime


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


#  \\192.168.100.100\SmartTech Learning Group\2023\9-8\video_files\«Account» folder of Services.mp4 True
#  \\192.168.100.100\SmartTech Learning Group\\2023\9-8\video_files\«Account» folder of Services.mp4  false


# file_path_list = listdir(r'\\192.168.100.100\SmartTech Learning Group\2021 ')
# print(file_path_list)
