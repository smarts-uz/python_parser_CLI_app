import shutil
import os

from django_orm.db.db_functions import get_file_paths
from file_copy.file_copy_functions import remove_unsupported_chars, create_txt_file_content
from file_copy.find_https_link import find_https, create_url_file


# def copy_file(path,file):
#     shutil.copy2(file, path)

def copy_file_with_custom_date(src, dst, custom_date):
    # Copy the file
    file_dst = shutil.copy(dst, src)
    # Set the custom date
    os.utime(file_dst, (custom_date.timestamp(), custom_date.timestamp()))




def copy_all_files(group,path):
    match group.absent:
        case False:
            file = get_file_paths(pk=group.pk)
            file_path = file[0]
            file_name_ex = file[1]
            file_name = file[2]
            type = file[3]
            match group.content:
                case None:
                    print(f'{group.pk}\'s file {group.file_path} copy process starting size: {group.size} duration: {group.duration}')
                    copy_file_with_custom_date(src=path,dst=file_path,custom_date=group.date)
                case _:
                    content = remove_unsupported_chars(text=group.content)
                    destination_file_path = os.path.join(path, f'{content}.{type}')
                    if os.path.isfile(destination_file_path):
                        print(f'This {group.pk}\'s data is  already copied')
                    else:
                        try:
                            print(
                                f'{group.pk}\'s file {group.file_path} copy process starting size: {group.size} duration: {group.duration}')
                            # shutil.copy2(file_path, path)
                            copy_file_with_custom_date(src=path, dst=file_path, custom_date=group.date)
                            os.rename(os.path.join(path, file_name_ex), destination_file_path)
                            create_txt_file_content(content=group.content, path=path,
                                                                 txt_name=f'{content}.{type}',custom_date=group.date)
                        except:
                           pass
        case True:
            content = remove_unsupported_chars(text=group.content)
            http = find_https(group.content)

            match http:
                case []:
                    create_txt_file_content(content=group.content, path=path, txt_name=f'{content}',custom_date=group.date)
                    print(f'{group.pk}\'s data message copied with name {content}')
                case _:
                    print(http[0])
                    create_url_file(url=http[0],name=content,path=path,custom_date=group.date)
                    print(f'{group.pk}\'s created url file {http}')

