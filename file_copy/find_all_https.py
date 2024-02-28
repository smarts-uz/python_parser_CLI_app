import  re

def find_http(text):
    matching = re.findall(r'https?.*',text)
    return matching