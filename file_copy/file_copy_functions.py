import os.path


def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list

def remove_hashtag(text):
    import re
    main_text = text
    # result = re.findall(r'#\w+?', text)
    result = re.findall(r'\#.*', text)
    text = re.sub(r'\#.*','',text)
    if text == "":
        text= main_text
    hashtag_text = ''.join(result)
    hashtag_list = hashtag_text.split('#')

    return text, hashtag_list[1:]


def remove_http(http):
    import re
    pattern = 'https?://w?w?w?[.]?'
    word = re.sub(pattern,' ',http.lower())
    return word

def remove_unsupported_chars(text):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    text = remove_http(text)

    text_1 = remove_hashtag(text)
    text = text_1[0]
    hashtag_list = text_1[1]

    for char in unsupchar:
        text = text.replace(char,' ')

    if len(list(text)) > 10:
        six_word = text.split(' ')[:10]
        six_word =' '.join(six_word)
    else:
        six_word=text

    return six_word.strip(),hashtag_list


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