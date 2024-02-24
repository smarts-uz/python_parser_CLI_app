import os

from main_functions.file_copy_process import file_copy_pr

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from log3 import Logger
current_l = Logger('current', 'w')
from django_orm.db.db_functions import  get_execution_data_from_id
from main_functions.process_cmdline import cmd_parsing_process, cmd_copy_process
from main_functions.run import run_parsing, run_copy


def main_execute(ex_id):
    cmd_parsing_process()
    execution = get_execution_data_from_id(ex_id=ex_id)
    print(f'id: {ex_id} name:{execution.name}')
    match execution.status:
        case 'completed':
            print(f'status: {execution.status}, already done!')
        case 'new' | 'parsing_process':
            print(f'current status: {execution.status}')
            if cmd_parsing_process() !=None:
                print(cmd_parsing_process())
            match cmd_parsing_process():
                case None:
                    run_parsing(ex_id)
                case _:
                    if ex_id in cmd_parsing_process():
                        print('This parsing already running. Please wait until end!!')
                    else:
                        run_parsing(ex_id)

        case 'parsing_ok' | 'filemove_process':
            print(f'current status: {execution.status}')
            cmd_copy_process()
            match cmd_copy_process():
                case None:
                    run_copy(ex_id)
                case _:
                    if ex_id in cmd_copy_process():
                        print('This move process already running. Please wait until end')
                    else:
                        run_copy(ex_id)

        










