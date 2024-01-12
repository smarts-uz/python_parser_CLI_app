import os
from dotenv import load_dotenv
import shutil
from .functions import correct_data_title, correct_video_title, correct_post_title, correct_file_location, correct_url_name, create_link, create_video_note, create_folder_to_save
from rich import print
from log3 import Logger
statistic = Logger('statictics', 'a')


def create_dirs_all(list_of_data, main_folder_name,name_list):
    load_dotenv()
    path_to_save = os.getenv('PATH_TO_SAVE')
    base_dir = os.getenv('BASE_DIR')
    try:
        index_of_group = int(main_folder_name)
        main_folder_name = name_list[index_of_group]
    except:
        pass

    path_to_save_last = create_folder_to_save(path_to_save, main_folder_name)
    for item in list_of_data:
        if item[1] != None:
            if item[0] is None:
                from_name = 'Unknown_user'
            elif item[0].isspace():
                from_name = 'Unknown_user'
            elif item[0].find('/') or item[0].find('\\') or item[0].find(':'):
                from_name = 'Unknown_user'
            else:
                from_name = item[0].strip()
            channel_text = correct_post_title(item[1])
            content = item[2]
            description = item[3]
            video_duration = item[4]
            post_title = correct_post_title(item[1])
            video_title = correct_video_title(content, post_title)
            file_path = item[-2]
            if len(channel_text) == 1:
                # actual_path = path_to_save
                actual_path = path_to_save_last
                if content.startswith('files') or content.startswith('photos'):
                    for i in channel_text:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            file_location = base_dir + '\\' + file_path
                            shutil.copy(file_location, actual_path_dir)
                            with open(f'{actual_path_dir}{from_name}.tmnote', 'x', encoding='UTF-8') as file:
                                file.write(f'''From_name: {from_name}\n{video_title}''')
                            msg = "[purple]"+actual_path + content + '___Succes_2!'
                            statistic.log(msg)
                            print(msg)

                        except Exception as e:
                            try:
                                with open(f'{actual_path_dir}{from_name}.tmnote', 'a', encoding='UTF-8') as file:
                                    file.write(f'''\n{video_title}''')
                            except:
                                msg = f'[purple] {content} - unable to create tmnote'
                                statistic.log(msg)
                                print(msg)
                            pass
                elif content.startswith('video'):
                    # actual_path = path_to_save
                    actual_path = path_to_save_last
                    for i in post_title:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            file_location = base_dir + '\\' + file_path
                            shutil.copy(file_location, actual_path_dir + video_title)
                            create_video_note(actual_path_dir, video_title, description, video_duration, from_name)
                            msg = "[purple]"+actual_path_dir + video_title + '___Succes_1!'
                            statistic.log(msg)
                            print(msg)
                        except:
                            msg = f'[red] {content} - unable to create folder'
                            statistic.err(msg)
                            print(msg)
                            pass
                elif content.startswith('https'):
                    for i in channel_text:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            create_link(actual_path_dir, correct_url_name(content), content)
                        except:
                            msg = f'[red] {content} - unable to create link'
                            statistic.err(msg)
                            print(msg)
                            pass
            else:
                if content.startswith('files') or content.startswith('photos'):
                    # actual_path = path_to_save
                    actual_path = path_to_save_last
                    file_location = base_dir + '\\' + file_path
                    for i in channel_text:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        shutil.copy(file_location, actual_path)
                        with open(f'{actual_path}{from_name}.tmnote', 'x', encoding='UTF-8') as file:
                            file.write(f'From_name: "{from_name}"\n{video_title}')
                        msg = "[purple]"+actual_path + content + '___Succes_2!'
                        statistic.log(msg)
                        print(msg)
                    except:
                        try:
                            with open(f'{actual_path}{from_name}.tmnote', 'a', encoding='UTF-8') as file:
                                file.write(f'''\n{video_title}''')
                        except:
                            msg = f'[red] {content} - unable to create tmnote'
                            statistic.err(msg)
                            print(msg)
                            pass
                        pass
                elif content.startswith('video'):
                    # actual_path = path_to_save
                    actual_path = path_to_save_last
                    file_location = base_dir + '\\' + file_path
                    for i in post_title:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        shutil.copy(file_location, actual_path + video_title)
                        create_video_note(actual_path, video_title, description, video_duration, from_name)
                        msg = "[purple]"+actual_path + video_title + '___Succes_2!'
                        statistic.log(msg)
                        print(msg)
                    except:
                        msg = f'[red] {content} - unable to create note'
                        statistic.err(msg)
                        print(msg)
                        pass
                elif content.startswith('https'):
                    # actual_path = path_to_save
                    actual_path = path_to_save_last
                    for i in channel_text:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        create_link(actual_path, correct_url_name(content), content)
                    except:
                        msg = f'[red] {content} - unable to create link';statistic.err(msg);print(msg)
                        pass
                else:
                    pass
