import os.path
import time

from rich import print

from Check_path.check_src_path import check_path_Src
from Telegram.tg_bot import send_error_msg
from file_copy.copy_shutil_func.slice_target_content_len import slice_target_content_lens
from file_copy.silicing_long_words.slicing_words_file import slice_words
from log3 import Logger


def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list

def remove_hashtag(text):
    import re
    text = text.replace('\n',' ')
    text = text.replace('  ',' ')
    main_text = text
    hashtag_list = []
    # result = re.findall(r'#.*?', text) old
    if '#' in text and '|' in text and text.index('#') < text.index('|'):
        text = text
    else:
        result = re.findall(r'\#\w.*', text)
        text1 = re.sub(r'\#\w.*', '', text)
        if text1 == "":
            text = text
        else:
            text = text1
        hashtag_text = ''.join(result)
        unsupchar = ["\\", "/", '"', ":", "<", ">", "|", "*", "?"]
        for char in unsupchar:
            hashtag_text = hashtag_text.replace(char,' ')
        hashtag_text = hashtag_text.replace('  ',' ')

        hashtag_list = hashtag_text.split('#')



    return text, hashtag_list[1:]


def remove_http(http):
    import re
    if 'http' in http or 'HTTP' in http:
        pattern = '[hH][tT]{2}[pP][sS]?://[wW]{3}?[.]?'
        word = re.sub(pattern,' ',http)
    else:
        word = http
    replace_char = ['exchanges/','search?q=']
    for char in replace_char:
        word = word.replace(char,' ')
        word = word.replace('  ',' ')
    return word

def remove_unsupported_chars(text,hashtag=False):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?" ]
    text = remove_http(text)
    hashtag_list = []
    if hashtag == False:
        text_1 = remove_hashtag(text)
        text = text_1[0]
        hashtag_list = text_1[1]

    for char in unsupchar:
        text = text.replace(char,' ')
    text = text.replace('\n',' ')
    text = text.replace('  ',' ')
    text = text.replace('  ',' ')


    return text.strip(),hashtag_list



current = Logger('current', 'a')

from dotenv import load_dotenv
load_dotenv()

def create_txt_file_content(path,custom_date,txt_name,group_id,destination_file_path,content=None,):
    check_path_Src()
    txt_name = slice_words(text=f'{path}/{txt_name}',destination_file_path = destination_file_path)
    if txt_name == True:
        text = f""""{content}"
        """
        # txt_name = slice_target_content_lens(path=path,filename=txt_name)
        if os.path.isfile(f'{destination_file_path}.txt'):
            print(f'This txt [purple4 bold]{destination_file_path}.txt file is already created!')
        else:
            try:
                with open(f'{destination_file_path}.txt', mode="w", encoding='utf-8') as file:
                    print(f'Created txt file [green_yellow bold]{destination_file_path}.txt')
                    file.write(text)
                os.utime(f'{destination_file_path}.txt', (custom_date.timestamp(), custom_date.timestamp()))
            except FileExistsError as e:
                print(f'[red]Error {e}')
                send_error_msg(error=e,group_id=group_id)
                current.err(e)

    else:
        pass




# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\