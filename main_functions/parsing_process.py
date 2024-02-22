from django_orm.db.db_functions import get_path_by_execution_id
from parsing.foreach_parser import parsing_foreach


def main_parsing_process(ex_id):
    execution = get_path_by_execution_id(ex_id)
    print(execution)
    name = execution[0]
    path = execution[1]
    status = execution[3]
    current = execution(ex_id)[2]
    parsing_data = parsing_foreach(path=path,execution_id=ex_id,channel_name=name,current_html=current)



# main_parsing_process(ex_id=258)