import datetime
import time

from Json.json_file_checker import file_check
from parsing.file_func.check_file_absent import check_file_absent


def filter_message(datas,path,channel_name,execution_id):
    channel_data = []
    group_data = []
    for i in datas:
        if 'from' in i:
            if i['type'] == "service":
                continue
            else:
                timestamp = i['date_unixtime']
                date = datetime.datetime.fromtimestamp(int(timestamp))
                from_name = i['from']
                message_id = i['id']
                try:
                    reply_to_message_id = i['reply_to_message_id']
                except:
                    reply_to_message_id = None
                try:
                    file = i['file']
                    check = check_file_absent(path=path, file_path=file)
                    absent = check[0]
                    byte = check[1]

                except:
                    file = None
                    absent = True
                    byte = None
                try:
                    photo = i['photo']
                except:
                    photo = None
                try:
                    text = ""
                    content = i['text']
                    # print(content)
                    for t in content:
                        if type(t) == str:
                            text += t
                        elif type(t) == dict:
                            text += t['text']
                        # match type(t):
                        #
                        #     case str: case not support str
                        #         text += t
                        #     case dict:
                        #         text += t['text']
                except:
                    text = None
                if text == '':
                    text = None
                file_path = file_check(file=file,photo=photo)
                if from_name == channel_name:
                    channel_data.append({message_id: {
                        'message_id': message_id,
                        'from_name': from_name,
                        'text': text,
                        'date': date,
                        'file_path': file_path,
                        'reply_to_msg_id': reply_to_message_id,
                        'path': path,
                        'execution_id': execution_id,
                        'message_details': 'json_message',
                    }})
                else:
                    group_data.append({message_id: {
                        'content': text,
                        'date': date,
                        'message_id': message_id,
                        'replied_message_id': reply_to_message_id,
                        'file_path': file_path,
                        'tg_channel_id': None,
                        'execution_id': execution_id,
                        'target': None,
                        'absent': absent,
                        'byte': byte,
                        'html': 'json',
                        'message_details': 'json_message',
                        'replied_message_details': 'json_message',
                        'path' : path,
                        'channel_name' : channel_name
                    }})


    return channel_data,group_data
