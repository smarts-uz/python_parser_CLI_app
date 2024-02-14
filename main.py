import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import click

from main_functions.main_func import main_execute, main_parsing
from process_cmdline import cmd_process
from run import run_parsing
from django_orm.db.db_functions import get_path_by_execution_id, get_all_execution_status_pk
from django_orm.db.db_save import insert_or_get_execution, insert_data_to_db
from parsing.foreach_parser import parsing_foreach

from parsing.parser import final_result_info
from rich import print
from django_orm.main import save_data_to_db, update_database
from django_orm.db.save_to_db import read_group_content, read_main_folder_name
from structure_foldering.structuring_folder import create_dirs_all
from log3 import Logger
import subprocess
#3log
current = Logger('current', 'w');history = Logger('history', 'a');statistic = Logger('statictics', 'a')

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


@parser.command(help="Create folders, change .env file to adjusments")
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
    insert_or_get_execution(path=path,name=name)
    print(f'[cyan]Collecting end!!!!')

@parser.command()
@click.option('--ex_id',help='Execution id')
def parsing(ex_id):
    execute = main_parsing(ex_id)






@parser.command()
def execute():

    executions =get_all_execution_status_pk()
    for exe in executions:
        e = main_execute(exe)









try:
    if __name__ == '__main__':parser()
    msg = "Successful parser-cli app run";current.log(msg);history.log(msg);statistic.log(msg);print(f'[green]{msg}')
except Exception as errs:
    msg = f"[red]Error: {errs}"
    current.log(msg);current.err(errs);history.log(msg);history.err(errs);statistic.log(msg);statistic.err(errs)
    print(f'[red]{msg}')
