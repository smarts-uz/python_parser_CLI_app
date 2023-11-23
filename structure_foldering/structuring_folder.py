import os
from dotenv import load_dotenv
import shutil
from .functions import correct_data_title, correct_video_title, correct_post_title, correct_file_location, correct_url_name


def create_dirs_all(list_of_data):
    load_dotenv()
    path_to_save = os.getenv('PATH_TO_SAVE')
    base_dir = os.getenv('BASE_DIR')
    for item in list_of_data:
        if item[1] != None:
            from_name = item[0]
            channel_text = correct_post_title(item[1])
            content = item[2]
            description = item[3]
            video_duration = item[4]
            data = correct_data_title(item[5])
            post_title = correct_post_title(item[1])
            video_title = correct_video_title(content, post_title)
            if len(channel_text) == 1:
                actual_path = path_to_save
                if content.startswith('files') or content.startswith('photos'):
                    for i in channel_text:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            file_location = correct_file_location(content, data, base_dir)
                            shutil.copy2(file_location, actual_path_dir)
                            with open(f'{actual_path_dir}{from_name}.txt', 'x', encoding='UTF-8') as file:
                                file.write(f'From_name: {from_name}')
                        except:
                            pass
                        print(actual_path + content + '___Succes_2!')
                elif content.startswith('video'):
                    actual_path = path_to_save  # There should be path of directory where you want to save all videos
                    for i in post_title:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            file_location = correct_file_location(content, data, base_dir)
                            shutil.copy2(file_location, actual_path_dir + video_title)
                            with open(f'{actual_path_dir}{video_title}.txt', 'x', encoding='UTF-8') as file:
                                try:
                                    file.write(f'''Description: {description}
Video_duration: {video_duration}
From_name: {from_name}''')
                                except:
                                    file.write(f'''Description: None
Video_duration: {video_duration}
From_name: {from_name}''')
                        except:
                            pass
                        print(actual_path_dir + video_title + '___Succes_1!')
                elif content.startswith('https'):
                    for i in channel_text:
                        actual_path_dir = actual_path + i + "\\"
                        if not os.path.exists(actual_path_dir):
                            try:
                                os.mkdir(actual_path_dir)
                            except:
                                pass
                        try:
                            with open(f'{actual_path_dir}{correct_url_name(content)}.url', 'x', encoding='UTF-8') as file:
                                file.write("""
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=""" + content + """
IconIndex=13
HotKey=0
IconFile=C:\Windows\System32\SHELL32.dll
""")
                        except:
                            pass
            else:
                if content.startswith('files') or content.startswith('photos'):
                    actual_path = path_to_save
                    file_location = correct_file_location(content, data, base_dir)
                    for i in channel_text:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        shutil.copy2(file_location, actual_path)
                        with open(f'{actual_path}{from_name}.txt', 'x', encoding='UTF-8') as file:
                            file.write(f'From_name: {from_name}')
                    except:
                        pass
                    print(actual_path + content + '___Succes_2!')
                elif content.startswith('video'):
                    actual_path = path_to_save  # There should be path of directory where you want to save all videos
                    file_location = correct_file_location(content, data, base_dir)
                    for i in post_title:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        shutil.copy2(file_location, actual_path + video_title)
                        with open(f'{actual_path}{video_title}.txt', 'x', encoding='UTF-8') as file:
                            try:
                                file.write(f'''Description: {description}
Video_duration: {video_duration}
From_name: {from_name}''')
                            except:
                                file.write(f'''Description: None
Video_duration: {video_duration}
From_name: {from_name}''')
                    except:
                        pass
                    print(actual_path + video_title + '___Succes_2!')
                elif content.startswith('https'):
                    actual_path = path_to_save
                    for i in channel_text:
                        actual_path = actual_path + i + "\\"
                        if not os.path.exists(actual_path):
                            try:
                                os.mkdir(actual_path)
                            except:
                                pass
                    try:
                        with open(f'{actual_path}{correct_url_name(content)}.url', 'x', encoding='UTF-8') as file:
                            file.write("""
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=""" + content + """
IconIndex=13
HotKey=0
IconFile=C:\Windows\System32\SHELL32.dll""")
                    except:
                        pass



