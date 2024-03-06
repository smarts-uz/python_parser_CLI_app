import os.path
from rich import print

from Telegram.tg_bot import send_error_msg
from file_copy.copy_shutil_func.slice_target_content_len import slice_target_content_lens
from file_copy.silicing_long_words.slicing_words_file import slice_words


def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list

def remove_hashtag(text):
    import re
    main_text = text
    hashtag_list = []
    # result = re.findall(r'#.*?', text) old
    if '#' in text and '|' in text and text.index('#') < text.index('|'):
        text = text
    else:
        result = re.findall(r'\#\w.*', text)
        text = re.sub(r'\#\w.*', '', text)
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
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    text = remove_http(text)
    hashtag_list = []
    if hashtag == False:
        text_1 = remove_hashtag(text)
        text = text_1[0]
        hashtag_list = text_1[1]

    for char in unsupchar:
        text = text.replace(char,' ')
    text = text.replace('  ',' ')
    text = text.replace('  ',' ')
    if len(list(text)) > 10:
        six_word = text.split(' ')[:10]
        six_word =' '.join(six_word)
    else:
        six_word=text

    return six_word.strip(),hashtag_list





def create_txt_file_content(path,custom_date,txt_name,group_id,content=None):
    txt_name = slice_words(text=txt_name)
    if txt_name != '':
        text = f""""{content}"
        """
        txt_name =slice_target_content_lens(path=path,filename=txt_name)
        if os.path.isfile(f'{path}/{txt_name}.txt'):
            print(f'This txt [purple4 bold]{path}/{txt_name}.txt file is already created!')
        else:
            try:
                with open(f'{path}/{txt_name}.txt', mode="w", encoding='utf-8') as file:
                    print(f'Created txt file [green_yellow bold]{path}/{txt_name}.txt')
                    file.write(text)
                os.utime(f'{path}/{txt_name}.txt', (custom_date.timestamp(), custom_date.timestamp()))
            except Exception as e:
                print(e)
                send_error_msg(error=e,group_id=group_id)
    else:
        pass




# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\