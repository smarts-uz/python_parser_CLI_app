import shutil

from file_copy.file_copy_functions import remove_unsupported_chars
from file_copy.find_https_link import find_https, create_url_file


def create_readme_file(dst_path, content, date, file_path=None):
    match file_path:
        case None:
            http = find_https(content=content)
            file_name = remove_unsupported_chars(content,hashtag=False)
            file_name = file_name.replace('  ',' ')
            match http:
                case []:
                    with open(f'{dst_path}/{file_name}.txt', 'w', encoding='utf=8') as file:
                        file.write(content)
                case _:
                    create_url_file(url=http, name=file_name, path=dst_path, custom_date=date)
        case _:
            shutil.copy(file_path, dst_path)
