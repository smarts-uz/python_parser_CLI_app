from django_orm.db.db_functions import get_path_by_execution_id
from django_orm.db.db_save import insert_data_to_db
from parsing.foreach_parser import parsing_foreach


def main_parsing_process(ex_id):
    execution = get_path_by_execution_id(ex_id)
    print(execution)
    name = execution[0]
    path = execution[1]
    status = execution[3]
    current = execution[2]
    parsing_data = parsing_foreach(path=path,execution_id=ex_id,channel_name=name,current_html=current)
    save_info = insert_data_to_db(parsing_data)
    channel_count = save_info[0]
    group_count = save_info[1]
    print(f'[green]Success')
    print(f'[cyan]Channel: [blue]exist:{channel_count[0]}, [green]new:{channel_count[1]}')
    print(f'[cyan]Group: [blue]exist:{group_count[0]}, [green]new:{group_count[1]}')



main_parsing_process(ex_id=264)