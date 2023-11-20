from bs4 import BeautifulSoup
import json
from os import listdir
from datetime import datetime
import pytz


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
def prepare_group_info(list):
    dict_learning_id = list[0]
    dict_all_content = list[2]
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
                     joined, description, video_duration, type_of_content])
            else:
                reply_id = int(y[5])
                text = get_text(dict_learning_id, reply_id)
                try:
                    from_name = y[6]
                except:
                    from_name = None
                test.append(
                    [from_name, text, content, data_title, message_details, msg_id, replied_message_details, reply_id,
                     joined, type_of_content])
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


# E:\SmartTech Learning Group\2021
def get_htmls(path):
    list_dir = listdir(path)
    result = []
    for i in list_dir:
        hmtl_path = path + '\\' + i
        path_content = listdir(hmtl_path)
        for k in path_content:
            if k.endswith('html'):
                last_path = hmtl_path + '\\' + k
                result.append(last_path)
    return result

#  get_htmls(r'E:\SmartTech Learning Group\2021')

