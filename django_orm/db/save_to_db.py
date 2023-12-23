from .models import channel_content, group_content
from parsing.functions import correct_info, correct_info_id, correct_info_name, get_from_name_for_group, prepare_name_info


def read_channel_db():
    dict_r = list(channel_content.objects.values_list('message_id', 'text'))
    result = {}
    for i in dict_r:
        result[i[0]] = i[1]
    return result


def get_info_from_db():
    myresult = list(group_content.objects.filter(joined=0).values_list("from_name", "message_id", "replied_message_id"))
    return myresult


def get_info_from_db_2():
    myresult = list(group_content.objects.filter(from_name=None).values_list("message_id"))
    return myresult


def update_group_name(dict_id):
    for x, y in dict_id.items():
        group_content.objects.filter(message_id=x, from_name=None).update(from_name=y)
        print(f"Message - {x}, updated with name - {y}!")


def update_group_text():
    dict_text_id = read_channel_db()
    for x, y in dict_text_id.items():
        group_content.objects.filter(channel_text=None, replied_message_id=x).update(channel_text=y)
        print(f"Message - {x}, updated with text - {y}!")


def add_parser_channel_id():
    info_channel = list(channel_content.objects.values_list('message_id', 'id'))
    info_group = list(group_content.objects.values_list('message_id', 'replied_message_id'))
    result_dict = {}
    for k in info_group:
        for i in info_channel:
            if k[1] == i[0]:
                result_dict[k[0]] = i[1]
    for x, y in result_dict.items():
        msg_id = x
        id = y
        group_content.objects.filter(message_id=msg_id).update(parser_channel_id=id)
        print(f'Message: {msg_id} is updated with id={id}')


def update_folder_name():
    list_of_folder_name = list(channel_content.objects.values_list('message_id', 'main_folder_name'))
    for i in list_of_folder_name:
        group_content.objects.filter(replied_message_id=i[0], main_folder_name=None).update(main_folder_name=i[1])
        print(f'Message_replied: {i[0]} is updated with folder_name={i[1]}')


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
    return 'Db has been updated!'


def read_group_content(main_folder_name):
    info_list = list(group_content.objects.filter(main_folder_name=main_folder_name).values_list("from_name", "channel_text", "content", "description", "video_duration", "data", 'filepath', 'main_folder_name'))
    return info_list[1000:1500]


def read_main_folder_name():
    name_list_1 = list(group_content.objects.values_list('main_folder_name').distinct())
    name_result = []
    for i in name_list_1:
        if i[0] != None:
            name_result.append(*i)
    return name_result


