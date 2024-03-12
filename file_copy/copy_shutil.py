import os
from rich import print
from django_orm.db.db_functions import get_file_paths, update_target_group
from file_copy.copy_shutil_func.copy_file_custom_date import copy_file_with_custom_date
from file_copy.copy_shutil_func.slice_target_lenth import slice_target_len
from file_copy.file_copy_functions import remove_unsupported_chars, create_txt_file_content
from file_copy.http.find_https_link import find_https, create_url_file



def copy_all_files(group,path):
    match group.absent:
        case False:
            file = get_file_paths(pk=group.pk)
            file_path = file[0]
            file_name_ex = slice_target_len(src=file_path,dst=path)
            # file_name_ex = file[1]
            file_name = file[2]
            type = file[3]
            match group.content:
                case None:
                    print(f'[bright_green]{group.pk}\'s File {group.file_path.split('/')[1]} copy process starting Size: [green bold]{group.size} Duration: [green bold]{group.duration}')

                    if os.path.isfile(os.path.join(path,file_name_ex)):
                        print(f'This [purple4]{group.pk}\'s File {group.file_path.split('/')[1]} is  already copied')
                    else:
                        copy_file_with_custom_date(src=file_path,dst=path,custom_date=group.date,group_id=group.pk,file_name=file_name_ex)
                case _:
                    content = remove_unsupported_chars(text=group.content,hashtag=True)[0]
                    destination_file_path = os.path.join(path, f'{content}.{type}')
                    if os.path.isfile(destination_file_path):
                        print(f'This [purple4]{group.pk}\'s data is  already copied')
                    else:
                        try:
                            print(
                                f'[bright_green]{group.pk}\'s File [green bold]{group.file_path.split('/')[1]} copy process starting Size: [green bold]{group.size} Duration: [green bold]{group.duration} Content: [green bold]{group.content}')
                            copy_file_with_custom_date(src=file_path, dst=path, custom_date=group.date,group_id=group.pk)
                            os.rename(os.path.join(path, file_name_ex), destination_file_path)
                            create_txt_file_content(content=group.content, path=path,
                                                                 txt_name=f'{content}.{type}',custom_date=group.date)
                        except:
                           pass
        case True:
            match group.content:
                case None:
                    if group.file_path != None:
                        print(f'[red]This file not exists [bright_green]tg_group_id:{group.pk}  [red bold]{group.file_path}')
                case _:
                        content = remove_unsupported_chars(text=group.content)[0]
                        https = find_https(group.content)
                        match https:
                            case []:
                                create_txt_file_content(content=group.content, path=path, txt_name=f'{content}',custom_date=group.date,group_id=group.pk)
                                print(f'[bright_green]{group.pk}\'s data message copied with name {content}')
                            case _:

                                for http in https:
                                    create_url_file(url=http,path=path,custom_date=group.date,group_id=group.pk)
                                    print(f'[blue]{group.pk}\'s created [dark blue]url file {http}')
                                if len(https) > 1:
                                    create_txt_file_content(content=group.content, path=path, txt_name=f'{content}',
                                                            custom_date=group.date, group_id=group.pk)
            update_target_group(pk=group.pk,target=path)

