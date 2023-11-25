import click

from . import main

@click.group()
def parser():
    pass

parser.add_command(commands.parsing)
parser.add_command(commands.create_folders)
parser.add_command(commands.update_db_content)