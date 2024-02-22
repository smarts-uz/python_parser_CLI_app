import os
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
    print(f'id: {ex_id} name:{execution.name} current status:{execution.status}')
    match execution.status:
        case 'completed':
            pass
        case 'new':
            print(cmd_parsing_process())
            match cmd_parsing_process():
                case None:
                    run_parsing(ex_id)
                case _:
                    if ex_id in cmd_parsing_process():
                        print('This parsing already running. Please wait until end!!')
                    else:
                        run_parsing(ex_id)
        case 'parsing_process':
            pass

        case 'parsing_ok':
            cmd_copy_process()
            match cmd_copy_process():
                case None:
                    run_copy(ex_id)
                case _:
                    if ex_id in cmd_copy_process():
                        print('This move process already running. Please wait until end')
                    else:
                        run_copy(ex_id)

        case 'parsing_ok':
            print(f'Ready to copy to folder {execution.pk}')










# main_parsing(ex_id=259)