import os

from file_copy.copy_shutil import copy_file_with_custom_date
from file_copy.file_copy_functions import remove_unsupported_chars
from file_copy.http.find_https_link import find_https, create_url_file


def create_readme_file(dst_path, content, date, main_path=None,file_path=None):
    match file_path:
        case None:
            https = find_https(content=content)
            chars = remove_unsupported_chars(content)
            hashtag_list = chars[1]
            match https:
                case []:
                    if hashtag_list != []:
                        for hashtag in hashtag_list:
                            if len(hashtag) > 100:
                                hashtag_name = hashtag[:100]
                            else:
                                hashtag_name = hashtag
                            with open(f'{dst_path}/#{hashtag_name}.txt', 'w', encoding='utf=8') as file:
                                file.write(f'#{hashtag}')
                    else:
                        print('Hashtag not found')
                case _:
                    for http in https:
                        create_url_file(url=http,path=dst_path, custom_date=date)
        case _:
            src_file_path = f'{main_path}/{file_path}'
            new_dst = copy_file_with_custom_date(src=src_file_path,dst=dst_path,custom_date=date)
            file_type = file_path.split('.')[-1]
            if content !=None:
                new_name = remove_unsupported_chars(content)[0]
                os.rename(new_dst,f'{dst_path}/{new_name}.{file_type}')

