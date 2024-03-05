

def correct_url_name(url):
    if 'https://' in url:
        url = url.replace('https://',' ')
    if  'http://' in url:
        url = url.replace('http://',' ')
    if 'www.' in url:
        url = url.replace('www.',' ')
    if 'search?q=' in url:
        url = url.replace('search?q=',' ')
    if 'exchanges?' in url:
        url = url.replace('exchanges?',' ')
    url = url.replace('/', ' ')
    url = url.replace('  ',' ')

    return url.title()






