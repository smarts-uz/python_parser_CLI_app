import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from Telegram.tg_bot import send_error_msg
from log3 import Logger
from file_copy.silicing_long_words.slicing_long_word_list import slice_long_words_list
from file_copy.create_txt_files.create_txt_file_for_folders import create_readme_file
from file_copy.remove_unsupported_chars.remove_http_for_folders import correct_http_for_create_folder
from file_copy.remove_unsupported_chars.remove_list_unsupported_chars import remove_list_unsupported_chars
from rich import print
# ---Testing Structure Folsers function---
from dotenv import load_dotenv
load_dotenv()


from file_copy.file_copy_functions import strip_space_list_element, remove_hashtag,remove_unsupported_chars

current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')


def remove_special_characters(text):
    # filtered_text = (''.join(char for char in text if char.isalpha() or char.isspace()))
    filtered_text = (''.join(char for char in text if char.isalpha() or char.isspace()))
    return filtered_text


#
def correct_filename(text,channel_name):
    root = f'{os.getenv('PATH_TO_SAVE')}{channel_name.strip()}/'
    text1 = text.split('\n')
    for line in text1:
        line = line.strip()
        # line=remove_special_characters(line)
        if '|' in line:
            # my_list = line.split(' | ')
            my_list = line.split('|')

            my_list.reverse()
            for i,word in enumerate(my_list):
                update_text = remove_hashtag(text=word)[0]
                if 'http' in update_text or 'HTTP' in update_text:
                    update_text = correct_http_for_create_folder(text=update_text)
                my_list[i] = update_text
            my_list = slice_long_words_list(my_list)
            my_list = strip_space_list_element(text=my_list)
            my_list = remove_list_unsupported_chars(my_list)
            my_list1 = '/'.join(my_list)
            path = f"{root}{my_list1}"
            return path

        else:
            text = remove_hashtag(text=text)[0]
            http = correct_http_for_create_folder(text=text)

            match http:
                case '':
                    mylist = text.split(' ')

                    if len(mylist) > 7:
                        my_list = mylist[0:7]
                    else:
                        my_list = mylist
                    text = ' '.join(my_list)
                    # new_text = remove_special_characters(text)
                    new_text = remove_unsupported_chars(text)[0]
                    path = f"{root}{new_text}"

                    return path
                case _:
                    path = f'{root}{http}'
                    return path


def file_creator(actual_path1,channel_name,custom_date,tg_channel_id,file_path=None,main_path=None,):
    # hashtag_list = remove_hashtag(text=actual_path1)[1]
    actual_path = correct_filename(actual_path1,channel_name)
    actual_path = actual_path.strip()
    if not os.path.exists(actual_path):
        try:
            os.makedirs(actual_path)
            create_readme_file(dst_path=actual_path, content=actual_path1, date=custom_date, file_path=file_path,
                               main_path=main_path,tg_channel_id=tg_channel_id)
            if custom_date != None:
                os.utime(actual_path, (custom_date.timestamp(), custom_date.timestamp()))
            print(f"Directory created successfully: [pink4 bold]{actual_path}")
            return actual_path
        except Exception as e:
            print(f'[red]Error {e}')
            send_error_msg(error=e,tg_channel_id=tg_channel_id)
            current.err(e)
            history.err(e)
            statistic.err(e)

    else:
        print(f"Directory already exists: [purple4 bold]{actual_path}")
        return actual_path

