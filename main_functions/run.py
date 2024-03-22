import subprocess
import sys

from django_orm.db.db_functions import change_status_execution


def run_parsing(ex_id):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'parsing', f"--ex_id={ex_id}"])
    code = pros.wait()
    match code:
        case 0:
            print(f'Parsing running process completed successfully execution_id={ex_id}')
            print(f'Copy file process starting execution_id={ex_id}')
            run_copy(ex_id)
        case _:
            print(f'Warning parsing problem code is :{code}')
    return code


def run_execute(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'execute', f"--ex_id={ex_id}"])
    code = execute.wait()
    return code

def run_json_execute(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'json-execute', f"--ex_id={ex_id}"])
    code = execute.wait()
    return code

def run_copy(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'file-copy', f"--ex_id={ex_id}"])
    code = execute.wait()
    match code:
        case 0:
            print('File copy process completed successfully')
        case _:
            print(f'Warning copy problem code is: {code}')
    return code

def run_json(ex_id):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'json-pars', f"--ex_id={ex_id}"])
    code = pros.wait()
    match code:
        case 0:
            print(f'Parsing running process completed successfully execution_id={ex_id}')
            print(f'Copy file process starting execution_id={ex_id}')
            run_copy(ex_id)
        case _:
            print(f'Warning parsing problem code is :{code}')
    return code
