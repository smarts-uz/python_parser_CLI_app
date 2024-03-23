import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()

from django_orm.db.db_save import insert_or_get_execution
from main_functions.run import run_execute


def collector_html(path,name):
    print('collecting starting')
    executions_list = insert_or_get_execution(path=path, name=name)
    for execution in executions_list:
        run_execute(ex_id=execution['id'])
    print(f'[cyan]Collecting end!!!!')