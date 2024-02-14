from django_orm.db.db_functions import get_path_by_execution_id
from django_orm.db.db_save import insert_data_to_db
from parsing.foreach_parser import parsing_foreach
from process_cmdline import cmd_process
from run import run_parsing


def main_execute(exe):
    if exe['status'] == 'parsing_process' or exe['status'] == 'new':
        get_process = cmd_process()
        print(exe)
        print(get_process)
        if get_process != None and get_process[-1].split('=')[1] == str(exe['pk']):
            print('This parsing is already running please wait until end!!!')
        else:
            print(f'parsing is starting ex_id: {exe['pk']}')
            pars = run_parsing(exe['pk'])
            if pars == 0:
                print('ok')
            else:
                print('warning! problem')





def main_parsing(ex_id):
    try:
        path = get_path_by_execution_id(ex_id)[1]
        channel_name = get_path_by_execution_id(ex_id)[0]
        parsing_data = parsing_foreach(path, ex_id, channel_name)
        save_info = insert_data_to_db(parsing_data)
        channel_count = save_info[0]
        group_count = save_info[1]
        print(f'[green]Success')
        print(f'[cyan]Channel: [blue]exist:{channel_count[0]}, [green]new:{channel_count[1]}')
        print(f'[cyan]Group: [blue]exist:{group_count[0]}, [green]new:{group_count[1]}')
    except Exception as e:
        print(e)

