import time
from pprint import pprint

import natsort

from Check_path.check_src_path import check_path_parsing
from django_orm.db.db_functions import change_status_execution, update_execution_current
from parsing.functions import search_html
from parsing.other_functions import current_html_name, html_search
from parsing.parser_v_2 import Pars
from natsort import natsorted

def parsing_foreach(path,execution_id,channel_name,current_html=None):
    check_path_parsing()
    fname_list = html_search(path)
    channel_content_list = []
    group_content_list = []
    if current_html !=None:
        current_path = f'{path}\\{current_html}'
        start_index = fname_list.index(current_path)
        fname_list = fname_list[start_index:]
    change_status_execution(id=execution_id, parsing_process=True)
    for folder in natsort.os_sorted(fname_list):
        parsing = Pars(file_path=folder, execution_id=execution_id, channel_name=channel_name)
        parsing_data =parsing.main_msg()
        channel_content_list.append(natsort.os_sorted(parsing_data[0]))
        group_content_list.append(natsort.os_sorted(parsing_data[1]))
    return [channel_content_list, group_content_list]
