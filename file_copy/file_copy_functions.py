import os.path


def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list

def remove_hashtag(text):
    import re
    result = re.findall(r'#\w+', text)
    for res in result:
        text = text.replace(res, '')

    return text


def remove_http(http):
    import re
    pattern = 'https?://w?w?w?[.]?'
    word = re.sub(pattern,'',http.lower())
    return word

def remove_unsupported_chars(text):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    text = remove_http(text)
    text = remove_hashtag(text)
    for char in unsupchar:
        text = text.replace(char,' ')
    for char in text.split(' '):
        if len(char) > 15:
            text  = text.replace(char,char[:15])
    if len(list(text)) > 6:
        six_word = text.split(' ')[:6]
        six_word =' '.join(six_word)
    else:
        six_word=text
    return six_word


def create_txt_file_content(path,custom_date,txt_name,content=None,):

    text = f""""{content}"
"""
    if os.path.isfile(f'{path}\\{txt_name}.txt'):
        print(f'This txt {path}\\{txt_name}.txt file is already created!')
    else:
        with open(f'{path}\\{txt_name}.txt',mode="w", encoding='utf-8') as file:
            print(f'{path}\\{txt_name}.txt')
            file.write(text)
        os.utime(f'{path}\\{txt_name}.txt', (custom_date.timestamp(), custom_date.timestamp()))



def slice_long_words(text):
    for word in text:
        if len(word) > 20:
            index = text.index(word)
            text[index] = word[:20]
        else:
            text = text
    return text

# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\