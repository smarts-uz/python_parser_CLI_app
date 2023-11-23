import click
from parsing.parser import final_result_info

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.main import save_data_to_db, update_database
from django_orm.db.save_to_db import read_group_content
from structure_foldering.structuring_folder import create_dirs_all


@click.group('Parser')
def parser():
    pass


@parser.command()
@click.option('--path', prompt='Path of directory', help='Here you should enter the path of files to parse')
def parsing(path):
    info_list = final_result_info(path)
    save_data_to_db(info_list)
    click.echo('Success!')


@parser.command()
def update_db_content():
    update_database()
    click.echo('Success!')


@parser.command()
def create_folders():
    info_list = read_group_content()
    create_dirs_all(info_list)
    click.echo('Success!')


if __name__ == '__main__':
    parser()
