from django_orm.db.db_functions import change_status_execution, update_execution_current
from parsing.functions import search_html
from parsing.other_functions import current_html_name
from parsing.parser_v_2 import Pars


def parsing_foreach(path,execution_id,channel_name):
    fname_list = search_html(path)
    channel_content_list = []
    group_content_list = []
    for folder in fname_list:
        current_html = current_html_name(folder)
        change_status_execution(id=execution_id,parsing_process=True)
        update_execution_current(id=execution_id,current=current_html)
        parsing = Pars(folder,execution_id,channel_name)
        ready_information = parsing.main_msg()[1]
        channel_content = parsing.main_msg()[0]
        channel_content_list.append(channel_content)
        group_content_list.append(ready_information)
    return [channel_content_list, group_content_list]
