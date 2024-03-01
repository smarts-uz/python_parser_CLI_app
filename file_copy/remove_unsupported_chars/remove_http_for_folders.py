import re

def correct_http_for_create_folder(text):
    # match = re.findall('https?.*',text.lower())
    match = re.findall('[hH][tT]{2}[pP][Ss]?.*',text)
    url_name = ''.join(match).replace('//','/').split('/')[-1]

    return url_name




