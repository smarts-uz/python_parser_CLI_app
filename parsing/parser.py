from .functions import get_html, save_json, prepare_group_info, get_from_name_joined, get_from_name, get_htmls, correct_time_data
# from save_to_db import save_mysql_channel, save_mysql_group, save_mysql_video


# В данной функции происходит вся магия)
# функция парсит все необходимые данные и на выходе дает список словарей со всей спарсенной информацией
def get_info(html):
    page_body = html.find('div', class_='history')
    messages_1 = page_body.find_all('div', class_='message default clearfix')
    messages_2 = page_body.find_all('div', class_='message default clearfix joined')
    dict_learning_id = {}
    dict_learning_content = {}
    dict_all_content = {}
    for i in messages_1:
        message_details = i.get('id')  # message_details
        msg_id = ''.join(i.get('id').split('message'))  # message_id
        body = i.find('div', class_='body')
        from_name = ' '.join(body.find('div', class_='from_name').get_text().split())  # from_name
        title = body.find('div', class_='pull_right date details').get('title') # time_data
        joined = False
        try:
            if from_name == 'SmartTech Learning':
                text = ' '.join(body.find('div', class_='text').get_text().split())  # text
                intMsg = int(msg_id)
                dict_learning_id[intMsg] = [text]
                dict_learning_id[intMsg].append(title)
                dict_learning_id[intMsg].append(from_name)
            elif from_name == 'SmartTech Learning Group':
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')  # replied_message_details
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))  # replied_message_id
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                dict_all_content[msg_id] = [replied_message_details]
                dict_all_content[msg_id].append(title)
                dict_all_content[msg_id].append(message_details)
                dict_all_content[msg_id].append(joined)
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')  # file
                    dict_learning_content[reply_id] = [file_link]
                    dict_learning_content[reply_id].append(from_name)
                    dict_all_content[msg_id].append(file_link)
                    if box.find('a', class_='video_file_wrap clearfix pull_left'):
                        video_box = box.find('a', class_='video_file_wrap clearfix pull_left')
                        video_duration = ' '.join(video_box.find('div', class_='video_duration').get_text().split())
                        try:
                            description = ' '.join(body.find('div', class_='text').get_text().split())
                        except:
                            description = None
                        dict_all_content[msg_id].append(description)
                        dict_all_content[msg_id].append(video_duration)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')  # url
                        dict_learning_content[reply_id] = [url]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text')  # text
                        if text_content.find('strong'):
                            text_content_1 = text_content.get_text()
                            result_text = f'**{text_content_1}**'
                        elif text_content.find('i'):
                            text_content_2 = text_content.get_text()
                            result_text = f'*{text_content_2}*'
                        else:
                            result_text = text_content.get_text()
                        dict_learning_content[reply_id] = [result_text]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(result_text)
                dict_all_content[msg_id].append(reply_id)
                dict_all_content[msg_id].append(from_name)
            else:
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                dict_all_content[msg_id] = [replied_message_details]
                dict_all_content[msg_id].append(title)
                dict_all_content[msg_id].append(message_details)
                dict_all_content[msg_id].append(joined)
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    dict_learning_content[reply_id] = [file_link]
                    dict_learning_content[reply_id].append(from_name)
                    dict_all_content[msg_id].append(file_link)
                    if box.find('a', class_='video_file_wrap clearfix pull_left'):
                        video_box = box.find('a', class_='video_file_wrap clearfix pull_left')
                        video_duration = ' '.join(video_box.find('div', class_='video_duration').get_text().split())
                        try:
                            description = ' '.join(body.find('div', class_='text').get_text().split())
                        except:
                            description = None
                        dict_all_content[msg_id].append(description)
                        dict_all_content[msg_id].append(video_duration)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id] = [url]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text')
                        if text_content.find('strong'):
                            text_content_1 = text_content.get_text()
                            result_text = f'**{text_content_1}**'
                        elif text_content.find('i'):
                            text_content_2 = text_content.get_text()
                            result_text = f'*{text_content_2}*'
                        else:
                            result_text = text_content.get_text()
                        dict_learning_content[reply_id] = [result_text]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(result_text)
                dict_all_content[msg_id].append(reply_id)
                dict_all_content[msg_id].append(from_name)
        except:
            pass
    for i in messages_2:
        message_details = i.get('id')  # message_details
        msg_id = ''.join(i.get('id').split('message'))  # message_id
        body = i.find('div', class_='body')
        title = body.find('div', class_='pull_right date details').get('title')  # time_data
        joined = True
        if body.find('div', class_='reply_to details'):
            reply_id_details = body.find('div', class_='reply_to details')
            replied_message_details = reply_id_details.find('a').get('href')
            reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
            try:
                if int(reply_id):
                    pass
            except:
                reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                reply_id = reply_id_list[1]
            dict_all_content[msg_id] = [replied_message_details]
            dict_all_content[msg_id].append(title)
            dict_all_content[msg_id].append(message_details)
            dict_all_content[msg_id].append(joined)
            try:
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    try:
                        dict_learning_content[reply_id].append(file_link)
                    except:
                        dict_learning_content[reply_id] = [file_link]
                    dict_all_content[msg_id].append(file_link)
                    if box.find('a', class_='video_file_wrap clearfix pull_left'):
                        video_box = box.find('a', class_='video_file_wrap clearfix pull_left')
                        video_duration = ' '.join(video_box.find('div', class_='video_duration').get_text().split())
                        try:
                            description = ' '.join(body.find('div', class_='text').get_text().split())
                        except:
                            description = None
                        dict_all_content[msg_id].append(description)
                        dict_all_content[msg_id].append(video_duration)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id].append(url)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text')
                        if text_content.find('strong'):
                            text_content_1 = text_content.get_text()
                            result_text = f'**{text_content_1}**'
                        elif text_content.find('i'):
                            text_content_2 = text_content.get_text()
                            result_text = f'*{text_content_2}*'
                        else:
                            result_text = text_content.get_text()
                        dict_learning_content[reply_id].append(result_text)
                        dict_all_content[msg_id].append(result_text)
            except:
                pass
            dict_all_content[msg_id].append(reply_id)
        else:
            try:
                text = ' '.join(body.find('div', class_='text').get_text().split())
                dict_learning_id[int(msg_id)] = [text]
                dict_learning_id[int(msg_id)].append(title)
            except:
                pass
    results = [dict_learning_id, dict_learning_content, dict_all_content]
    return results


def final_result_info(path):
    fname_list = get_htmls(path)
    channel_content_list = []
    group_content_list = []
    for i in fname_list:
        main_html = get_html(i)  #  Здесь мы передаем путь к mhtml-файлу и происходит первичный парсинг через bs4
        result = get_info(main_html)  #  Результат выше указанной функции(get_html) мы передаем в данную функцию(get_info), где и происходит основной сбор данных(парсинг)
        save_json(result)  #  На данном этапе мы сохраняем полученныет данные в json формат, для первичного визуального анализа и дальнейшей обработки данных
        prepare_info = prepare_group_info(result)  #  Здесь происходит первичная обработка данных
        dict_reply = get_from_name_joined(result)  #  Здесь мы получаем словарь с replied_id и from_name
        ready_information = get_from_name(prepare_info, dict_reply) #  Данная функция возвращает на выходе готовый список данных из Learning Group для отправки в бд
        channel_content = result[0]
        channel_content_list.append(channel_content)
        group_content_list.append(ready_information)
    # for i in group_content_list:
    #     for k in i:
    #         print(k)
    return [channel_content_list, group_content_list]


# final_result_info('E:\SmartTech Learning Group\\2022')
