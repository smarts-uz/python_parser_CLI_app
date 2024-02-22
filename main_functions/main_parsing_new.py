from django_orm.db.db_functions import get_path_by_execution_id
from django_orm.db.db_save import insert_data_to_db
from parsing.foreach_parser import parsing_foreach
from log3 import Logger
current_l = Logger('current', 'w')

def main_parsing(ex_id):
    try:
        path = get_path_by_execution_id(ex_id)[1]
        channel_name = get_path_by_execution_id(ex_id)[0]
        parsing_data = parsing_foreach(path=path,execution_id=ex_id,channel_name=channel_name)
        save_info = insert_data_to_db(parsing_data)
        channel_count = save_info[0]
        group_count = save_info[1]
        print(f'[green]Success')
        print(f'[cyan]Channel: [blue]exist:{channel_count[0]}, [green]new:{channel_count[1]}')
        print(f'[cyan]Group: [blue]exist:{group_count[0]}, [green]new:{group_count[1]}')
    except Exception as e:
        current_l.log(e)
        print(e)


