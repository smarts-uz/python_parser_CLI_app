import subprocess
import sys

from django_orm.db.db_functions import change_status_execution


def run_parsing(ex_id):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'parsing', f"--ex_id={ex_id}"])
    code = pros.wait()
    match code:
        case 0:
            run_copy(ex_id)
        case _:
            print(f'Warning parsing problem code is :{code}')
    return code


def run_execute(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'execute', f"--ex_id={ex_id}"])
    code = execute.wait()
    return code


def run_copy(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'file-copy', f"--ex_id={ex_id}"])
    code = execute.wait()
    match code:
        case 0:
            change_status_execution(id=ex_id,completed=True)
        case _:
            print(f'Warning move problem code is: {code}')
    return code
