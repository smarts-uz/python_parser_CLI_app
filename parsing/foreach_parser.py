from pprint import pprint

import natsort

from django_orm.db.db_functions import change_status_execution, update_execution_current
from parsing.functions import search_html
from parsing.other_functions import current_html_name, html_search
from parsing.parser_v_2 import Pars
from natsort import natsorted

def parsing_foreach(path,execution_id,channel_name,current_html=None):
    fname_list = html_search(path)
    channel_content_list = []
    group_content_list = []
    if current_html !=None:
        current_path = f'{path}\\{current_html}'
        start_index = fname_list.index(current_path)
        fname_list = fname_list[start_index:]
    change_status_execution(id=execution_id, parsing_process=True)
    for folder in natsort.os_sorted(fname_list):
        parsing = Pars(folder, execution_id, channel_name)
        ready_information = parsing.main_msg()[1]
        channel_content = parsing.main_msg()[0]
        channel_content_list.append(channel_content)
        group_content_list.append(ready_information)
    return [channel_content_list, group_content_list]
