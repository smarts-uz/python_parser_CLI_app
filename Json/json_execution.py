from Json.json_search import json_search
from django_orm.db.db_functions import get_execution_data_from_id
from pprint import pprint

from main_functions.process_cmdline import cmd_copy_process, cmd_json_parsing_process
from main_functions.run import run_copy, run_json


def json_execution(ex_id):
    execution = get_execution_data_from_id(ex_id=ex_id)
    print(f'[cyan2]execution_id: {ex_id} name:{execution.name}')
    match execution.status:
        case 'completed':
            print(f'[sea_green2]status: {execution.status}, already done!')
        case 'new' | 'parsing_process':
            cmd_parsing = cmd_json_parsing_process()
            print(f'[sea_green1]current status: {execution.status}')
            match cmd_parsing:
                case []:
                    print(f'[dark_red]Execute command run parsing command execution_id={ex_id}')
                    run_json(ex_id)
                case _:
                    find_execution_cmd_line = list(
                        filter(lambda id: int(list(id.keys())[0]) == int(ex_id), cmd_parsing))
                    match find_execution_cmd_line:
                        case []:
                            print(f'[cyan3]Execute command run parsing command execution_id={ex_id}')
                            run_json(ex_id)
                        case _:
                            pprint(find_execution_cmd_line[0])
                            print('[cyan3]This parsing already running. Please wait until end!!')
        case 'parsing_ok' | 'filemove_process':
            print(f'[sea_green1]current status: {execution.status}')
            copy_cmd = cmd_copy_process()
            match copy_cmd:
                case []:
                    print(f'[cyan3]Execute command run copy command execution_id={ex_id}')
                    run_copy(ex_id)
                case _:
                    find_execution_cmd_copy_line = list(
                        filter(lambda id: int(list(id.keys())[0]) == int(ex_id), copy_cmd))
                    match find_execution_cmd_copy_line:
                        case []:
                            print(f'[cyan3]Execute command run copy command execution_id={ex_id}')
                            run_copy(ex_id)
                        case _:
                            pprint(find_execution_cmd_copy_line[0])
                            print('This file copy process already running. Please wait until end!!')