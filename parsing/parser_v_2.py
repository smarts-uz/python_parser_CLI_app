from pprint import pprint

from bs4 import BeautifulSoup


class Pars:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_html(self):
        HtmlFile = open(self.file_path, 'r', encoding='utf-8')
        source_code = HtmlFile.read()
        soup = BeautifulSoup(source_code, 'html.parser')
        return soup

    def parsing(self):
        soup = self.get_html()
        history = soup.find('div', class_="history")
        main_messages = history.find_all('div',class_='message default clearfix')
        duration = None
        size = None
        data = []

        # print(len(main_messages))
        for main_message in main_messages:
            msg_id = main_message['id'][7:]
            message_body = main_message.find('div',class_='body')
            date = message_body.find('div', class_='pull_right date details')['title']
            from_name = message_body.find('div',class_='from_name').get_text(strip=True)

            try:
                text = message_body.find('div',class_='text').get_text(strip=True)
            except :
                text = message_body.find('div', class_='text')
            try:
                media = message_body.find('div',class_='media_wrap clearfix')
                try:
                    file_url = media.find('a',class_='photo_wrap clearfix pull_left')['href']

                except Exception as e:
                    file_url = media.find('a', class_='media clearfix pull_left block_link media_voice_message')['href']
                    duration = media.find('a', class_='media clearfix pull_left block_link media_voice_message').find('div',class_='status details').get_text(strip=True)

                except Exception as e:
                    video = media.find('a',class_='video_file_wrap clearfix pull_left')
                    file_url = media.find('a',class_='video_file_wrap clearfix pull_left')['href']
                    duration = video.find('div',class_='video_duration').get_text(strip=True)

                except Exception as e:
                    file = media.find('a',class_='media clearfix pull_left block_link media_file')
                    file_url = media.find('a',class_='media clearfix pull_left block_link media_file')['href']
                    size = file.find('div',class_='status details').get_text(strip=True)





            except:
                media = None
                file_url = None
                duration = None
                size = None

            try:
                reply_to_message_id = message_body.find('div',class_='reply_to details').find('a')['href'][14:]

            except:
                reply_to_message_id = None

            data.append(
                {
                    "msg_id" : msg_id,
                    "text" : text,
                    "file" : file_url,
                    "duration" : duration,
                    "size" : size,
                    'reply_to_msg_id' : reply_to_message_id,
                    'date' :date
                }
            )
        return data


