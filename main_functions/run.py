import subprocess
import sys

def run_parsing(ex_id):
    pros = subprocess.Popen([f'{sys.executable}', 'main.py', 'parsing', f"--ex_id={ex_id}"])
    code = pros.wait()
    return code

def run_execute(ex_id):
    execute = subprocess.Popen([f'{sys.executable}', 'main.py', 'execute', f"--ex_id={ex_id}"])
    code = execute.wait()
    return code
