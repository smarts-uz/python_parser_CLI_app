import json
import time
from pprint import pprint
import natsort
from bs4 import BeautifulSoup
from django_orm.db.db_functions import change_status_execution, update_execution_current
from parsing.functions import correct_time_data, search_html
from parsing.other_functions import file_choose, choose_duration, folder_path,current_html_name, filtered_message


class Pars:
    def __init__(self, file_path,execution_id,channel_name):
        self.file_path = file_path
        self.execution_id = execution_id
        self.channel_name = channel_name

    def get_html(self):
        HtmlFile = open(self.file_path, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        soup = BeautifulSoup(source_code, 'html.parser')
        return soup

    def parsing(self):
        soup = self.get_html()
        main_folder_name = soup.find('div', class_='content').get_text(strip=True)
        history = soup.find('div', class_="history")
        main_messages = history.find_all('div', class_='message default clearfix')
        joined_messages = history.find_all('div', class_='message default clearfix joined')
        return main_messages, joined_messages

    def main_msg(self):
        current_html = current_html_name(self.file_path)
        path = folder_path(self.file_path)
        # path = None
        global ogg_url, photo_url, video_url, duration_ogg, duration_video,reply_to_details
        execution_id = None
        tg_channel_id = None
        duration = None
        size = None
        data = []
        data_g = []
        media = None
        file_url = None
        duration_ogg = None
        duration_video = None

        main_messages = self.parsing()[0]
        joined_messages = self.parsing()[1]
        for main_message in main_messages:
            clear_msg = filtered_message(main_message=main_message,execution_id=self.execution_id,path=path)

            print(f'[{current_html}] message_id: {clear_msg['message_id']} text: {clear_msg['content']} (parsed)')
            match clear_msg["from_name"]:
                case self.channel_name:

                    data.append(
                {clear_msg['message_id']:{
                    "message_id": clear_msg['message_id'],
                    "message_details": clear_msg['message_details'],
                    "text": clear_msg['content'],
                    "file_path": clear_msg['file_path'],
                    "duration": clear_msg['duration'],
                    "size": clear_msg['size'],
                    'reply_to_msg_id': clear_msg['replied_message_id'],
                    "replied_message_details": clear_msg['replied_message_details'],
                    'date':clear_msg['date'],
                    'from_name': clear_msg['from_name'],
                    'execution_id': self.execution_id,
                    'path' : path,
                    'byte' : clear_msg['byte']

                }})
                case _:
                    data_g.append(
                    {clear_msg['message_id']:{
                        "message_id": clear_msg['message_id'],
                        "message_details": clear_msg['message_details'],
                        "content": clear_msg['content'],
                        "file_path": clear_msg['file_path'],
                        "duration": clear_msg['duration'],
                        "size": clear_msg['size'],
                        "replied_message_details": clear_msg['replied_message_details'],
                        'replied_message_id': clear_msg['replied_message_id'],
                        'date': clear_msg['date'],
                        'tg_channel_id': tg_channel_id,
                        'execution_id': self.execution_id,
                        'path': path,
                        'channel_name': self.channel_name,
                        'html' : current_html,
                        'absent': clear_msg['absent'],
                        'byte' : clear_msg['byte']
                    }}
                )

        for joined_message in joined_messages:

            j_data = filtered_message(joined_message,self.execution_id,path)
            if j_data['replied_message_id'] == None and data != []:
                filtered_message_numbers = list(filter(lambda msg: int(list(msg.keys())[0]) < int(j_data['message_id']), data))
                filtered_message_numbers = natsort.os_sorted(filtered_message_numbers)
                if filtered_message_numbers != []:
                    channel_data = filtered_message_numbers[-1]
                    filtered_message_ids = [list(msg.keys())[0] for msg in filtered_message_numbers]
                    filtered_message_ids = natsort.os_sorted(filtered_message_ids)
                    # channel_data_id = natsort.os_sorted(filtered_message_ids)[-1]
                    channel_data_id = filtered_message_ids[-1]
                    # print(channel_data[channel_data_id]['date'])
                    # print(
                    #     f'{channel_data[channel_data_id]['date'].hour}:{channel_data[channel_data_id]['date'].minute}')
                    # print(j_data['date_text'])
                    # print('stop')
                    # if j_data['date'] == channel_data[channel_data_id]['date'] and self.channel_name == channel_data[channel_data_id]['from_name']:
                    if j_data['date_text'] == f'{channel_data[channel_data_id]['date'].hour}:{channel_data[channel_data_id]['date'].minute}' and self.channel_name == channel_data[channel_data_id]['from_name']:

                        data.append({j_data['message_id']: {
                            "message_id": j_data['message_id'],
                            "message_details": j_data['message_details'],
                            "text": j_data['content'],
                            "file_path": j_data['file_path'],
                            "duration": j_data['duration'],
                            "size": j_data['size'],
                            'reply_to_msg_id': j_data['replied_message_id'],
                            "replied_message_details": j_data['replied_message_details'],
                            'date': j_data['date'],
                            'from_name': channel_data[channel_data_id]['from_name'],
                            'execution_id': self.execution_id,
                            'path': path,
                            'byte' : j_data['byte']

                        }})
                        print(
                            f'This message send by channel:{j_data['message_details']} {j_data['content']} added to channel_list instead of group_list')
                    else:
                        data_g.append(
                {j_data['message_id']:{
                    'message_id': j_data['message_id'],
                    'message_details': j_data['message_details'],
                    'date': j_data['date'],
                    "replied_message_id": j_data['replied_message_id'],
                    'replied_message_details': j_data['replied_message_details'],
                    "content": j_data['content'],
                    "file_path": j_data['file_path'],
                    "duration": j_data['duration'],
                    "size": j_data['size'],
                    'execution_id': self.execution_id,
                    'tg_channel_id': tg_channel_id,
                    'path': path,
                    'channel_name': self.channel_name,
                    'html': current_html,
                    'absent': j_data['absent'],
                    'byte' : j_data['byte']
                }}
            )
            else:
                data_g.append(
                    {j_data['message_id']: {
                        'message_id': j_data['message_id'],
                        'message_details': j_data['message_details'],
                        'date': j_data['date'],
                        "replied_message_id": j_data['replied_message_id'],
                        'replied_message_details': j_data['replied_message_details'],
                        "content": j_data['content'],
                        "file_path": j_data['file_path'],
                        "duration": j_data['duration'],
                        "size": j_data['size'],
                        'execution_id': self.execution_id,
                        'tg_channel_id': tg_channel_id,
                        'path': path,
                        'channel_name': self.channel_name,
                        'html': current_html,
                        'absent': j_data['absent'],
                        'byte' : j_data['byte'],
                    }})

            print(f'[{current_html}] message_id: {j_data['message_id']} content: {j_data['content']} (parsed)')



        return [natsort.os_sorted(data),natsort.os_sorted(data_g)]

#
#
# --path="h:\Exports\SmartTech Learning Group\2021" --name="SmartTech Learning"
#
# # #
# a = Pars(file_path="h:/SmartTech Learning Group/2023/7-21/messages3.html",channel_name="SmartTech Learning",execution_id=123)
# pprint(a.main_msg()[0])