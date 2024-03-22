import re
import time


def correct_http_for_create_folder(text):
    text = text.strip()
    len(text)
    if len(text) > 1 and text[-1] == '/':
        list_text = list(text)
        list_text[-1] = ''
        text = ''.join(list_text)
    else:
        text = text
    match = re.findall('[hH][tT]{2}[pP][Ss]?.*',text)
    url_name = ''.join(match).replace('//','/').split('/')[-1]
    url_name = re.sub(r'search\?q=', '', url_name)
    unsupchar = ["\\", "/", '"', ":", "<", ">", "|", "*", "?",]
    for char in unsupchar:
        url_name = url_name.replace(char,' ')
    url_name = url_name.replace('  ',' ')
    url_name = url_name.replace('  ',' ')

    return url_name



