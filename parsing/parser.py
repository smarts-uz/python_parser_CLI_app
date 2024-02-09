from pprint import pprint

from django_orm.main import save_to_execution
from .functions import get_html, save_json, prepare_group_info, get_from_name_joined, get_from_name, search_html, \
    correct_time_data, folder_path
from .parser_v_2 import Pars


# функция парсит все необходимые данные и на выходе дает список словарей со всей спарсенной информацией
def get_info(html):
    main_folder_name = ' '.join(html.find('div', class_='text bold').get_text().split())
    page_body = html.find('div', class_='history')
    messages = page_body.find_all('div', class_='message default clearfix')
    messages_joined = page_body.find_all('div', class_='message default clearfix joined')
    dict_learning_id, dict_learning_content, dict_all_content = {}, {}, {}
    for i in messages:
        message_details = i.get('id')
        msg_id = ''.join(i.get('id').split('message'))
        body = i.find('div', class_='body')
        from_name = ' '.join(body.find('div', class_='from_name').get_text().split())  # from_name
        title = body.find('div', class_='pull_right date details').get('title') # time_data
        joined = False
        try:
            if from_name and body.find('div', class_='reply_to details') is None:
                    text = ' '.join(body.find('div', class_='text').get_text().split())  # text
                    intMsg = int(msg_id)
                    dict_learning_id[intMsg] = [text]
                    dict_learning_id[intMsg].append(title)
                    dict_learning_id[intMsg].append(from_name)
                    dict_learning_id[intMsg].append(main_folder_name)
            elif from_name and body.find('div', class_='reply_to details'):
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
    for i in messages_joined:
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
                dict_learning_id[int(msg_id)].append(main_folder_name)
            except:
                pass
    results = [dict_learning_id, dict_learning_content, dict_all_content, main_folder_name]
    return results


def final_result_info(path):

    fname_list = search_html(path)
    channel_content_list = []
    group_content_list = []

    for folder in fname_list:
        f_path = folder_path(folder)
        parsing = Pars(folder)
        main_folder_name = parsing.parsing()[2]
        ready_information = parsing.joined_messages()
        channel_content = parsing.main_msg()
        channel_content_list.append(channel_content)
        group_content_list.append(ready_information)

        save_to_execution(name=main_folder_name,path=f_path,status='in_process')

    return [channel_content_list, group_content_list]



    # for i in fname_list:
    #     main_html = get_html(i)
    #     result = get_info(main_html)
    #     save_json(result)
    #     prepare_info = prepare_group_info(result, i)
    #     dict_reply = get_from_name_joined(result)
    #     ready_information = get_from_name(prepare_info, dict_reply)
    #     channel_content = result[0]
    #     channel_content_list.append(channel_content)
    #     group_content_list.append(ready_information)
    # return [channel_content_list, group_content_list]


# final_result_info('E:\SmartTech Learning Group\\2022')
