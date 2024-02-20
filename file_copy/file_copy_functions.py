def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list


def remove_unsupported_chars(text):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    for char in unsupchar:
        text = text.replace(char,' ')
    if len(text) >6:
        six_word = text.split(' ')[:6]
        six_word =' '.join(six_word)
    else:
        six_word=text
    return six_word


def create_txt_file_content(path,content=None,txt_name=None):


    text = f""""{content}"
"""
    with open(f'{path}\\{txt_name}.txt',mode="w", encoding='utf-8') as file:
        file.write(text)


# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\