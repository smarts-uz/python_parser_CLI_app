import os.path
from rich import print

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

    if '#' in text and '|' in text and text.index('#') > text.index('|'):
        result = re.findall(r'\#.*', text)
        text = re.sub(r'\#.*', '', text)
        hashtag_text = ''.join(result)
        hashtag_list = hashtag_text.split('#')

    else:
        text = text



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

def remove_unsupported_chars(text):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    text = remove_http(text)
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



def slice_long_words(text):
    for word in text:
        if len(word) > 100:
            index = text.index(word)
            text[index] = word[:100]
        else:
            text = text
    return text


def slice_words(text):
    if len(text) > 100:
        text = text[:100]
    else:
        text = text
    return text

def create_txt_file_content(path,custom_date,txt_name,content=None,):
    txt_name = slice_words(text=txt_name)
    text = f""""{content}"
"""
    if os.path.isfile(f'{path}\\{txt_name}.txt'):
        print(f'This txt [green_yellow bold]{path}\\{txt_name}.txt file is already created!')
    else:
        with open(f'{path}\\{txt_name}.txt',mode="w", encoding='utf-8') as file:
            print(f'Created txt file [green_yellow bold]{path}\\{txt_name}.txt')
            file.write(text)
        os.utime(f'{path}\\{txt_name}.txt', (custom_date.timestamp(), custom_date.timestamp()))



# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\