import click
from parsing.parser import final_result_info
from parsing.functions import logger_path

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from django_orm.main import save_data_to_db, update_database
from django_orm.db.save_to_db import read_group_content
from structure_foldering.structuring_folder import create_dirs_all
import logging
import os
module_name = os.path.splitext(os.path.basename(__file__))[0]
logger2 = logging.getLogger(module_name)
logger2.setLevel(logging.INFO)
# настройка обработчика и форматировщика для logger2
handler2 = logging.FileHandler(f"{logger_path()}/{module_name}.log", mode='a')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
# добавление форматировщика к обработчику
handler2.setFormatter(formatter2)
# добавление обработчика к логгеру
logger2.addHandler(handler2)
logger2.info(f"Running module {module_name}...")

errors = (AssertionError,AttributeError,EOFError,FloatingPointError,
    GeneratorExit,ImportError,IndexError,KeyError,MemoryError,
    NotImplementedError,OSError,OverflowError,ReferenceError,StopIteration,
    IndentationError,TabError,SystemError,SystemExit,TypeError,UnboundLocalError,UnicodeError,UnicodeEncodeError,
    UnicodeDecodeError,UnicodeTranslateError,ValueError,ZeroDivisionError,RuntimeError, TypeError, NameError,
    SyntaxError,Exception,ValueError,KeyboardInterrupt)


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

try:
    if __name__ == '__main__':
        parser()
    logger2.info("Successful run")
except errors as err:
    logger2.exception("Some kind of error, check log file")

