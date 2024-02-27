import shutil

from file_copy.file_copy_functions import remove_unsupported_chars ,remove_hashtag
from file_copy.find_https_link import find_https, create_url_file


def create_readme_file(dst_path, content, date, file_path=None):
    match file_path:
        case None:
            http = find_https(content=content)
            chars = remove_unsupported_chars(content)
            file_name = chars[0]
            hashtag_list = chars[1]
            file_name = file_name.replace('  ',' ')
            match http:
                case []:
                    for hashtag in hashtag_list:
                        if len(hashtag) > 100:
                            hashtag_name = hashtag[:100]
                        else:
                            hashtag_name= hashtag
                        with open(f'{dst_path}/#{hashtag_name}.txt', 'w', encoding='utf=8') as file:
                            file.write(f'#{hashtag}')
                case _:
                    create_url_file(url=http, name=file_name, path=dst_path, custom_date=date)
        case _:
            shutil.copy(file_path, dst_path)
