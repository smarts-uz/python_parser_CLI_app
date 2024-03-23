import time

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
import pyfiglet
from context_menu import menus
from main_functions.collector_func import collector_html
from main_functions.run import run_collector


def link(name,DIRECTORY):
    isometric1_text = pyfiglet.figlet_format('Parser CLI app', font='slant')
    print(isometric1_text)
    print(DIRECTORY,name[0])
    channel_name = input('Input Channel name: ')
    try:
        collector_html(path=name[0],name=channel_name)
    except Exception as e:
        print(e)
    input('press enter to close windows')


fc = menus.FastCommand('Parser CLI', type='DIRECTORY', python=link,params='DIR',command_vars=['DIRECTORY'])
fc_1 = menus.FastCommand('Parser CLI', type='DIRECTORY_BACKGROUND', python=link,params='DIR',command_vars=['DIRECTORY'])
fc.compile()
fc_1.compile()