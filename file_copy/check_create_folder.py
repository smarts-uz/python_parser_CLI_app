import os

from file_copy.create_txt_file_for_folders import create_readme_file

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django

django.setup()
from django_orm.db.models import *
# ---Testing Structure Folsers function---
from dotenv import load_dotenv

load_dotenv()

root = os.getenv('PATH_TO_SAVE')

from file_copy.file_copy_functions import strip_space_list_element, remove_hashtag, slice_long_words


# Testing value
# text='''No query results for model [Laravel\\Passport\\Client]., Laravel'''


def remove_special_characters(text):
    filtered_text = (''.join(char for char in text if char.isalpha() or char.isspace()))
    return filtered_text


#
def correct_filename(text):
    text = remove_hashtag(text=text)
    text1 = text.split('\n')
    for line in text1:
        line = line.strip()
        # line=remove_special_characters(line)
        if '|' in line:
            # my_list = line.split(' | ')
            my_list = line.split('|')
            my_list = strip_space_list_element(text=my_list)
            my_list.reverse()
            my_list = slice_long_words(my_list)
            my_list1 = '\\'.join(my_list)
            path = f"{root}{my_list1}"
            return path
        else:
            mylist = text.split(' ')
            if len(mylist) > 7:
                my_list = mylist[0:7]
            else:
                my_list = mylist
            text = ' '.join(my_list)
            new_text = remove_special_characters(text)
            path = f"{root}{new_text}"
            return path


def file_creator(actual_path1, file_path=None, custom_date=None):
    actual_path = correct_filename(actual_path1)
    if not os.path.exists(actual_path):
        os.makedirs(actual_path)
        create_readme_file(dst_path=actual_path, content=actual_path1, date=custom_date, file_path=file_path)
        if custom_date != None:
            os.utime(actual_path, (custom_date.timestamp(), custom_date.timestamp()))
        print(f"Directory created successfully: {actual_path}")
        return actual_path
    else:
        print(f"Directory already exists: {actual_path}")
        return actual_path


# print(file_creator(actual_path1=text))
# print(remove_special_characters(text))
# print(correct_filename(text))


#
# my_file = open("text_names_of_db.txt", "r")

# reading the file
# data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
# data_into_list = data.split("\n")
# print(data_into_list)
#
# # for the testing Structure Folder
# for a in data_into_list:
#     print(file_creator(actual_path1=a))
# my_file.close()
