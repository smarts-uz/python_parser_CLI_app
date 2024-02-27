import re

def check_http(text):
    match = re.findall('https?.*',text.lower())
    url_name = ''.join(match).replace('//','/').split('/')[-1]

    return url_name




#
# link = """http://elements.envato.com/ru/school-teacher-character-animation-scene-after-eff-KR5XWLN"""
#
# # check_http(text=link)