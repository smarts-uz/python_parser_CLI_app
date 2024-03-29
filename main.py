import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import click
import time

from Json.extracting_json import json_extract
from Json.json_execution import json_execution
from main_functions.collector_func import collector_html
from Telegram.tg_bot import send_error_msg
from main_functions.copy_file_process import file_copy_pr
from django_orm.db.db_functions import get_status_execution
from main_functions.main_parsing_new import main_parsing
from main_functions.parsing_process import main_parsing_process
from main_functions.main_func import main_execute
from main_functions.copy_file_main import copy_file
from django_orm.db.db_save import insert_or_get_execution, insert_or_get_execution_json
from main_functions.run import run_execute, run_json_execute
from parsing.parser import final_result_info
from rich import print
from django_orm.main import save_data_to_db, update_database
from django_orm.db.save_to_db import read_group_content, read_main_folder_name
from structure_foldering.structuring_folder import create_dirs_all
from log3 import Logger

#3log
current = Logger('current', 'a');history = Logger('history', 'a');statistic = Logger('statictics', 'a')

@click.group('Parser')
def parser():
    pass

@parser.command(help="Parse mhtml files from given path")
@click.option('--path', prompt='Path of directory', help='Here you should enter the path of files to parse')
def old_parsing(path):
    info_list = final_result_info(path)
    save_data_to_db(info_list)
    msg = 'Successful parsing!';history.log(msg);current.log(msg);statistic.log(msg);print(f'[green]{msg}')


@parser.command(help="Update db")
def update_db_content():
    update_database()
    msg = 'Successful database updating!';history.log(msg);current.log(msg);statistic.log(msg);print(f'[green]{msg}')


@parser.command(help="Create folders, change .env.example file to adjusments")
def create_folders():
    name_list = read_main_folder_name()
    for i in range(len(name_list)):
        print(f'{i} - {name_list[i]}')
    chosen_name = input('Выберите название группы для создания папок: ')
    info_list = read_group_content(chosen_name, name_list)
    create_dirs_all(info_list, chosen_name, name_list)
    msg = 'Successful creating folders!';
    history.log(msg);
    current.log(msg);
    statistic.log(msg);
    print(f'[green]!{msg}')

@parser.command(help="Collects all messages.html files path")
@click.option('--path',help='Html files folder path')
@click.option('--name',help='Channel name')
def collector(path,name):
    try:
        collector_html(path=path, name=name)

    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=errs)
        current.log(msg)
        print(f'[red]{msg}')

@parser.command(help="Collects all result.json files path")
@click.option('--path',help='json files folder path')
@click.option('--name',help='Channel name')
def collect_json(path,name):
    try:
        executions_list = insert_or_get_execution_json(path=path,name=name)
        for exe in executions_list:
            run_json_execute(ex_id=exe['id'])
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=errs)
        current.log(msg)
        print(f'[red]{msg}')



@parser.command(help="Parsing json file")
@click.option('--ex_id',help='Execution id')
def json_pars(ex_id):
    try:
        status = get_status_execution(ex_id)
        if status in ['new','parsing_process']:
            json_extract(execution_id=ex_id)
        else:
            print(f'Status is: {status}. Already parsed')
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=f'[ex_id:{ex_id}] {errs}')
        current.err(errs)
        print(f'[red]{msg}')

@parser.command(help='Run json_pars and copy commands step by step')
@click.option('--ex_id',help='Execution id')
def json_execute(ex_id):
    try:
        json_execution(ex_id=ex_id)
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=f'[ex_id:{ex_id}] {errs}')
        current.err(errs)
        print(f'[red]{msg}')

@parser.command(help="Parsing html file")
@click.option('--ex_id',help='Execution id')
def parsing(ex_id):
    try:
        status = get_status_execution(ex_id)
        match status:
            case 'new':
                main_parsing(ex_id)
            case 'parsing_process':
                main_parsing_process(ex_id=ex_id)
            case _:
                print(f'Status is: {status}. Already parsed')
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=f'[ex_id:{ex_id}] {errs}')
        current.err(errs)
        print(f'[red]{msg}')


@parser.command(help='Run parsing and copy commands step by step')
@click.option('--ex_id',help='Execution id')
def execute(ex_id):
    try:
        main_execute(ex_id=ex_id)
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=f'[ex_id:{ex_id}] {errs}')
        current.err(errs)
        print(f'[red]{msg}')




@parser.command(help='Copy files to folder which given in .env "Base dir = "')
@click.option('--ex_id',help='Execution id')
def file_copy(ex_id):
    try:
        status = get_status_execution(ex_id)
        match status:
            case 'parsing_ok':
                copy_file(ex_id)
            case 'filemove_process':
                file_copy_pr(ex_id=ex_id)
            case 'completed':
                print('This execution already completed!')
            case _:
                print('This execution is not ready to copy. You need to run parse command')
    except Exception as errs:
        msg = f"[red]Error: {errs}"
        send_error_msg(error=f'[ex_id:{ex_id}] {errs}')
        current.err(errs)
        print(f'[red]{msg}')



try:
    if __name__ == '__main__':parser()
    msg = "Successful parser-cli app run";current.log(msg);history.log(msg);statistic.log(msg);print(f'[green]{msg}')
except Exception as errs:
    msg = f"[red]Error: {errs}"
    send_error_msg(error=errs)
    current.log(msg);current.err(errs);history.log(msg);history.err(errs);statistic.log(msg);statistic.err(errs)
    print(f'[red]{msg}')
