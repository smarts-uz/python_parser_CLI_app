import datetime
import time
from parsing.file_func.check_file_absent import check_file_absent


def filter_message(datas,path,channel_name,execution_id):
    channel_data = []
    group_data = []
    for i in datas:
        if 'from' in i:
            timestamp = i['date_unixtime']
            date = datetime.datetime.fromtimestamp(int(timestamp))
            from_name = i['from']
            message_id = i['id']
            try:
                reply_to_message_id = i['reply_to_message_id']
            except:
                reply_to_message_id = None
            try:
                file_path = i['file']
                check = check_file_absent(path=path, file_path=file_path)
                absent = check[0]
                byte = check[1]
            except:
                file_path = None
                absent = None
                byte = None
            try:
                text = ""
                texts = i['text']
                for t  in texts:
                    text = f'{text} {t["text"]}'.strip()
            except:
                text = None
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
                    'message_details' : 'json_message'
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
                    'message_details' : 'json_message',
                    'replied_message_details' : 'json_message'
                }})

    return channel_data,group_data
