

def correct_url_name(url):
    if url[-1] == '/':
        url = url[:-1] + ''
    if 'http' in url.lower():
        host_name = url.split("//")
        if len(host_name) <=2:
            host_name = host_name[1]
        else:
            host_name = host_name[1:]
            host_name = '/'.join(host_name)
        if 'search?q' in host_name:
            name = host_name.split('search?q')[1]
            return name
        elif 't.me' in host_name:
            name = host_name.replace('/',' ')
            return name
        else:
            slicing = host_name.split('/')
            print(slicing)
            if len(slicing) >=3:
                name = slicing[-1]
                return name
            else:
                if 'www' in slicing[0]:
                    name = slicing[0].split('.')[1:]
                    name = '.'.join(name)
                    return name
                else:
                    return host_name








