from .models import *
from parsing.functions import correct_info, correct_info_id, correct_info_name, get_from_name_for_group, prepare_name_info
from log3 import Logger
from rich import print

statistic = Logger('statictics', 'a')
def read_channel_db():
    dict_r = list(TgChannel.objects.values_list('message_id', 'text'))
    result = {}
    for i in dict_r:
        result[i[0]] = i[1]
    return result


def get_info_from_db():
    myresult = list(TgGroup.objects.filter(joined=0).values_list("from_name", "message_id", "replied_message_id"))
    return myresult


def get_info_from_db_2():
    myresult = list(TgGroup.objects.filter(from_name=None).values_list("message_id"))
    return myresult


def update_group_name(dict_id):
    for x, y in dict_id.items():
        TgGroup.objects.filter(message_id=x, from_name=None).update(from_name=y)
        statistic.log(f"Message - {x}, updated with name - {y}!")
        print(f"[blue]Message - {x}, updated with name - {y}!")


def update_group_text():
    dict_text_id = read_channel_db()
    for x, y in dict_text_id.items():
        TgGroup.objects.filter(channel_text=None, replied_message_id=x).update(channel_text=y)
        statistic.log(f"Message - {x}, updated with text - {y}!")
        print(f"[blue]Message - {x}, updated with text - {y}!")


def add_parser_channel_id():
    info_channel = list(TgChannel.objects.values_list('message_id', 'id'))
    info_group = list(TgGroup.objects.values_list('message_id', 'replied_message_id'))
    result_dict = {}
    for k in info_group:
        for i in info_channel:
            if k[1] == i[0]:
                result_dict[k[0]] = i[1]
    for x, y in result_dict.items():
        msg_id = x
        id = y
        TgGroup.objects.filter(message_id=msg_id).update(parser_channel_id=id)
        statistic.log(f'Message: {msg_id} is updated with id={id}')
        print(f'[blue]Message: {msg_id} is updated with id={id}')


def update_folder_name():
    list_of_folder_name = list(TgChannel.objects.values_list('message_id', 'main_folder_name'))
    for i in list_of_folder_name:
        TgGroup.objects.filter(replied_message_id=i[0], main_folder_name=None).update(main_folder_name=i[1])
        statistic.log(f'Message_replied: {i[0]} is updated with folder_name={i[1]}')
        print(f'[blue]Message_replied: {i[0]} is updated with folder_name={i[1]}')


def update_db():
    list_of_msg_id = get_info_from_db()
    list_of_name_2 = correct_info(get_info_from_db_2())
    correct_list_id = correct_info_id(list_of_msg_id)
    correct_list_name = correct_info_name(list_of_msg_id)
    dict_id = get_from_name_for_group(correct_list_id, correct_list_name)
    update_group_name(prepare_name_info(dict_id, list_of_name_2))
    update_group_text()
    add_parser_channel_id()
    update_folder_name()
    statistic.log("[green]Db has been updated")
    return 'Db has been updated!'

def read_group_content(main_folder_name, list_of_group):
    try:
        index_of_group = int(main_folder_name)
        main_folder_name = list_of_group[index_of_group]
    except:
        pass
    info_list = list(TgGroup.objects.filter(main_folder_name=main_folder_name).values_list("from_name", "channel_text", "content", "description", "video_duration", "data", 'filepath', 'main_folder_name'))
    return info_list[1000:1200]


def read_main_folder_name():
    name_list_1 = list(TgGroup.objects.values_list('main_folder_name').distinct())
    name_result = []
    for i in name_list_1:
        if i[0] != None:
            name_result.append(*i)
    return name_result

def get_channel_id(msg_id):
    try:
       channel =  TgChannel.objects.get(message_id=msg_id)
       channel_id = channel.pk
    except TgChannel.DoesNotExist:
        channel_id =  None
    return  channel_id




def get_execution_id(name:str):
    return Execution.objects.get(name=name).pk





