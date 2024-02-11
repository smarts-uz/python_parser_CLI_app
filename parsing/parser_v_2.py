import json
from pprint import pprint

from bs4 import BeautifulSoup

from django_orm.db.db_functions import change_status_execution
from parsing.functions import correct_time_data, search_html
from parsing.other_functions import file_choose, choose_duration, folder_path


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
        path = folder_path(self.file_path)
        # path = None
        global ogg_url, photo_url, video_url, duration_ogg, duration_video
        execution_id = None
        duration = None
        size = None
        data = []
        data_g = []
        media = None
        file_url = None
        duration_ogg = None
        duration_video = None

        main_messages = self.parsing()[0]
        for main_message in main_messages:
            msg_id = main_message['id'][7:]
            message_body = main_message.find('div', class_='body')
            original_date = message_body.find('div', class_='pull_right date details')['title']
            date = correct_time_data(original_date)
            from_name = message_body.find('div', class_='from_name').get_text(strip=True)

            try:
                text = message_body.find('div', class_='text').get_text(strip=True)
            except:
                text = message_body.find('div', class_='text')
            try:
                media = message_body.find('div', class_='media_wrap clearfix')
                try:
                    photo_url = media.find('a', class_='photo_wrap clearfix pull_left')['href']
                except:
                    photo_url = None

                try:
                    ogg_url = media.find('a', class_='media clearfix pull_left block_link media_voice_message')['href']
                    duration_ogg = media.find('a',
                                              class_='media clearfix pull_left block_link media_voice_message').find(
                        'div', class_='status details').get_text(strip=True)

                except:
                    ogg_url = None
                    duration_ogg = None

                try:
                    video = media.find('a', class_='video_file_wrap clearfix pull_left')
                    video_url = media.find('a', class_='video_file_wrap clearfix pull_left')['href']
                    duration_video = video.find('div', class_='video_duration').get_text(strip=True)
                except:
                    video_url = None
                    duration_video = None

                try:
                    file = media.find('a', class_='media clearfix pull_left block_link media_file')
                    file_url = media.find('a', class_='media clearfix pull_left block_link media_file')['href']
                    size = file.find('div', class_='status details').get_text(strip=True)
                except:
                    file_url = None
                    size = None

            except:
                media = None
                file_url = None

                size = None

            file_path = file_choose(photo_url, ogg_url, video_url, file_url)
            duration = choose_duration(duration_ogg, duration_video)

            try:
                reply_to_message_id = message_body.find('div', class_='reply_to details').find('a')['href'][14:]

            except:
                reply_to_message_id = None
            if from_name == self.channel_name:
                data.append(
                {
                    "message_id": msg_id,
                    "text": text,
                    "file_path": file_path,
                    "duration": duration,
                    "size": size,
                    'reply_to_msg_id': reply_to_message_id,
                    'date': date,
                    'from_name': from_name,
                    'execution_id': self.execution_id,
                    'path' : path
                })
            else:
                data_g.append(
                    {
                        "message_id": msg_id,
                        "content": text,
                        "file_path": file_path,
                        "duration": duration,
                        "size": size,
                        'replied_message_id': reply_to_message_id,
                        'date': date,
                        'execution_id': self.execution_id,
                        'path': path,
                    }
                )


        return [data,data_g]
    def joined_messages(self):
        global ogg_url, photo_url, video_url, duration_ogg, duration_video
        # path = folder_path(self.file_path)
        path = None
        tg_channel_id = None
        execution_id = None
        duration = None
        size = None
        data = []
        media = None
        file_url = None
        joined_messages = self.parsing()[1]

        for joined_message in joined_messages:
            msg_details = joined_message['id']

            msg_id = joined_message['id'][7:]
            message_body = joined_message.find('div', class_='body')
            original_date = message_body.find('div', class_='pull_right date details')['title']
            date = correct_time_data(original_date)

            try:
                reply_to_details = message_body.find('div', class_='reply_to details').find('a')['href']
                reply_to_message_id = reply_to_details[14:]

            except:
                reply_to_details = None
                reply_to_message_id = None

            try:
                text = message_body.find('div', class_='text').get_text(strip=True)
            except:
                text = message_body.find('div', class_='text')
            try:
                media = message_body.find('div', class_='media_wrap clearfix')
                try:
                    photo_url = media.find('a', class_='photo_wrap clearfix pull_left')['href']
                except:
                    photo_url = None

                try:
                    ogg_url = media.find('a', class_='media clearfix pull_left block_link media_voice_message')['href']
                    duration_ogg = media.find('a',
                                              class_='media clearfix pull_left block_link media_voice_message').find(
                        'div', class_='status details').get_text(strip=True)

                except:
                    ogg_url = None
                    duration_ogg = None
                try:
                    video = media.find('a', class_='video_file_wrap clearfix pull_left')
                    video_url = media.find('a', class_='video_file_wrap clearfix pull_left')['href']
                    duration_video = video.find('div', class_='video_duration').get_text(strip=True)
                except:
                    video_url = None
                    duration_video = None

                try:
                    file = media.find('a', class_='media clearfix pull_left block_link media_file')
                    file_url = media.find('a', class_='media clearfix pull_left block_link media_file')['href']
                    size = file.find('div', class_='status details').get_text(strip=True)
                except:
                    file_url = None
                    size = None

            except:
                media = None
                file_url = None
                duration = None
                size = None

            file_path = file_choose(photo_url, ogg_url, video_url, file_url)
            duration = choose_duration(duration_ogg, duration_video)
            data.append({
                'message_id': msg_id,
                'message_details': msg_details,
                'date': date,
                "replied_message_id": reply_to_message_id,
                'replied_message_details': reply_to_details,
                "content": text,
                "file_path": file_path,
                "duration": duration,
                "size": size,
                'execution_id': self.execution_id,
                'tg_channel_id': tg_channel_id,
                'path': path
            })


        return data
