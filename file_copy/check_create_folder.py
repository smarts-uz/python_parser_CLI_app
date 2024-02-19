import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.db.models import *
# ---Testing Structure Folsers function---
from dotenv import load_dotenv
load_dotenv()
root=os.getenv('PATH_TO_SAVE')
# Testing value
text='''Accoola | Element | Corporate | Feedback'''
def remove_special_characters(text):
    # O'zgartirilgan matnda faqat harflar va probellar qoladi
    filtered_text = ''.join(char for char in text if char.isalpha() or char.isspace())
    return filtered_text
def correct_filename(text):
    text = text.split('\n')
    for line in text:
        # line=remove_special_characters(line)
        if '|' in line:
            my_list = line.split(' | ')
            my_list.reverse()
            my_list1 = '\\'.join(my_list)
            path = f"{root}{my_list1}"
            return path
        else:

            line=remove_special_characters(text)
            path = f"{root}{line}"
            return path
def file_creator(actual_path1):
    actual_path=correct_filename(actual_path1)
    if not os.path.exists(actual_path):
        os.makedirs(actual_path)
        print(f"Directory created sucsesfuly:{actual_path}")
        return True
    else:
        print(f"Directory already created:{actual_path}")
        return False
# print(file_creator(actual_path1=text))
