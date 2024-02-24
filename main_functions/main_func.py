import os
import time
from pprint import pprint

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

    execution = get_execution_data_from_id(ex_id=ex_id)
    print(f'id: {ex_id} name:{execution.name}')
    match execution.status:
        case 'completed':
            print(f'status: {execution.status}, already done!')
        case 'new' | 'parsing_process':
            cmd_parsing = cmd_parsing_process()
            print(f'current status: {execution.status}')
            match cmd_parsing:
                case []:
                    print(f'Execute command run parsing command execution_id={ex_id}')
                    run_parsing(ex_id)
                case _:
                    find_execution_cmd_line = list(filter(lambda id: int(list(id.keys())[0]) == int(ex_id), cmd_parsing))
                    match find_execution_cmd_line:
                        case []:
                            print(f'Execute command run parsing command execution_id={ex_id}')
                            run_parsing(ex_id)
                        case _:
                            pprint(find_execution_cmd_line[0])
                            print('This parsing already running. Please wait until end!!')
        case 'parsing_ok' | 'filemove_process':
            print(f'current status: {execution.status}')
            copy_cmd = cmd_copy_process()
            match copy_cmd:
                case []:
                    print(f'Execute command run copy command execution_id={ex_id}')
                    run_copy(ex_id)
                case _:
                    find_execution_cmd_copy_line = list(filter(lambda id: int(list(id.keys())[0]) == int(ex_id), copy_cmd))
                    match find_execution_cmd_copy_line:
                        case []:
                            print(f'Execute command run copy command execution_id={ex_id}')
                            run_copy(ex_id)
                        case _:
                            pprint(find_execution_cmd_copy_line[0])
                            print('This file copy process already running. Please wait until end!!')



        case _:
            print(f'Something went wrong status:{execution.status}')









