def strip_space_list_element(text):
    new_list = []
    for word in text:
        new_list.append(word.strip())

    return new_list


def remove_unsupported_chars(text):
    unsupchar = ["\\","/",'"',":", "<", ">" , "|" , "*" , "?"  ]
    for char in unsupchar:
        text = text.replace(char,' ')
    return text


def create_txt_file_content(size,duration,path,file_name,date,content=None,txt_name=None):


    text = f""""{content}"
{20*'-'}
{duration}
{20*'-'}
{file_name}
{20*'-'}
{size}
{20*'-'}
{date}
"""
    with open(f'{path}\\{txt_name}.txt',mode="w", encoding='utf-8') as file:
        file.write(text)


def create_txt_file(size,duration,path,file_name,date):
    text = f""""{None}"
{20 * '-'}
{duration}
{20 * '-'}
{file_name}
{20 * '-'}
{size}
{20 * '-'}
{date}
    """
    with open(f'{path}\\{file_name}.txt', mode="w", encoding='utf-8') as file:
        file.write(text)

# d:\testingparsing\PHP\HTML Parser\Paquettg.Php-Html-Parser\