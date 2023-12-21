from bs4 import BeautifulSoup
import json
from os import listdir
from datetime import datetime
import pytz
import os


# Здесь происходит первый парсинг через библиотеку BeautifulSoup
def get_html(file_path):
    HtmlFile = open(file_path, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


# Здесь сохраняются данные в формате json для дальнейшей обработки
def save_json(list):
    dict_learning_id = list[0]
    dict_learning_content = list[1]
    dict_all_content = list[2]
    with open('dict_learning_id.json', 'w', encoding='UTF-8') as file:
        json.dump(dict_learning_id, file, indent=4)
    with open('dict_learning_content.json', 'w', encoding='UTF-8') as file1:
        json.dump(dict_learning_content, file1, indent=4)
    with open('dict_all_content.json', 'w', encoding='UTF-8') as file2:
        json.dump(dict_all_content, file2, indent=4)
    return 'Done✅'


# Здесь происходит первичная обработка и корректировка данных из Learning Group
def prepare_group_info(list, mhtml_path):
    dict_learning_id = list[0]
    dict_all_content = list[2]
    main_folder_name = list[-1]
    test = []
    for x, y in dict_all_content.items():
        try:
            content = y[4]
            data_title = correct_time_data(y[1])
            message_details = y[2]
            msg_id = x
            replied_message_details = y[0]
            joined = y[3]
            type_of_content = define_type(content)
            if type_of_content in ['file', 'video', 'photo', 'audio']:
                file_path = get_file_path(content, mhtml_path, main_folder_name)
            else:
                file_path = None
            if len(y) > 7:
                reply_id = int(y[7])
                text = get_text(dict_learning_id, reply_id)
                description = y[5]
                video_duration = y[6]
                try:
                    from_name = y[8]
                except:
                    from_name = None
                test.append(
                    [from_name, text, content, data_title, message_details, msg_id, replied_message_details, reply_id,
                     joined, description, video_duration, type_of_content, file_path])
            else:
                reply_id = int(y[5])
                text = get_text(dict_learning_id, reply_id)
                try:
                    from_name = y[6]
                except:
                    from_name = None
                test.append(
                    [from_name, text, content, data_title, message_details, msg_id, replied_message_details, reply_id,
                     joined, type_of_content, file_path])
        except:
            pass
    return test


# Здесь также происходит обработка данных, а точнее получения заголовка к replied message
def get_text(dict_1, reply_id):
    try:
        text = dict_1[reply_id][0]
    except:
        text = None
    return text


# Функция возвращает словарь с replied_id и from_name, что также необходимо для конечной обработки данных
def get_from_name_joined(list2):
    dict_learning_content = list2[1]
    dict_reply_id_name = {}
    for x, y in dict_learning_content.items():
        try:
            name_type = define_type(y[1])
            if name_type == 'text':
                dict_reply_id_name[int(x)] = y[1]
            else:
                dict_reply_id_name[int(x)] = None
        except:
            dict_reply_id_name[int(x)] = None
    return dict_reply_id_name


# Данная функция возвращает конечные данные, готовые для отправки в бд
def get_from_name(list_info, dict_reply):
    result = list_info
    for i in list_info:
        if i[0] is None:
            for x, y in dict_reply.items():
                if i[7] == x:
                    i[0] = y
                else:
                    pass
    return result


def get_file_path(content, mhtml_path, main_folder_name):
    correct_mhtml_path = mhtml_path.split('\\')
    correct_mhtml_path[-1] = content
    result_list = []
    if main_folder_name in correct_mhtml_path:
        break_point = correct_mhtml_path.index(main_folder_name)
        for i in range(break_point, len(correct_mhtml_path)):
            result_list.append(correct_mhtml_path[i])
    result = '\\'.join(result_list)
    return result


def correct_time_data(data):
    first = data.split(' ')
    second = '-'.join(first[0].split('.')[::-1])
    result = f'{second} {first[1]}'
    timezone = pytz.timezone("Asia/Tashkent")
    parsed_date = datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
    date_with_timezone = timezone.localize(parsed_date)
    return date_with_timezone


def define_type(content):
    if content.startswith('http'):
        result = 'url'
    elif content.startswith('files'):
        result = 'file'
    elif content.startswith('video'):
        result = 'video'
    elif content.startswith('photos'):
        result = 'photo'
    elif content.startswith('voice'):
        result = 'audio'
    else:
        result = 'text'
    return result


def correct_info(list1):
    result = []
    for i in list1:
        result.append(i[0])
    return result


def correct_info_id(list_i):
    result = []
    for i in list_i:
        result.append(i[1])
    return result


def correct_info_name(list_n):
    result_name = []
    for i in list_n:
        result_name.append(i[0])
    return result_name


def get_from_name_for_group(list_of_msg_id, list_of_name):
    dict_result = {}
    for i in list_of_msg_id:
        index = list_of_msg_id.index(i)
        try:
            difference = list_of_msg_id[index + 1] - list_of_msg_id[index]
            dict_result[i] = [k for k in range(i, i+difference)]
            dict_result[i].append(list_of_name[index])
        except:
            dict_result[i] = [i]
            dict_result[i].append(list_of_name[index])
    return dict_result


def prepare_name_info(dict_info, list_name):
    result_dict = {}
    for i, k in dict_info.items():
        from_name = k[-1]
        for t in list_name:
            if t in k:
                result_dict[t] = from_name
    return result_dict


def search_html(path):
    html_files = []
    if '\\messages.html' in path:path = path[:-len('\\messages.html')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('message') and file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return html_files


def logger_path():
    year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
    logger_path = f"logs/{year}/{month}/{day}/"
    if not os.path.exists(logger_path):
        os.makedirs(logger_path)
    return logger_path