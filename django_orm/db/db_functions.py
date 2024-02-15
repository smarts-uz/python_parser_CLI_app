import os

import natsort

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_orm.settings')
import django
django.setup()
from .models import *


def get_path_by_execution_id(id):
    execution = Execution.objects.get(pk=id)
    return execution.name , execution.path

def change_status_execution(id,parsing_process=False,parsing_ok=False,filemove_process=False,completed=False):
    execution = Execution.objects.get(pk=id)
    if parsing_ok == True:
        execution.status = 'parsing_ok'
        print(f'[Execution]\'s id:{execution.pk} status changed to [green]parsing_ok')
        execution.save()
    elif parsing_process == True:
        execution.status = 'parsing_process'
        execution.save()
        print(f'[Execution]\'s id:{execution.pk} status changed to [green]parsing_process')
    elif filemove_process == True:
        execution.status = 'filemove_process'
        execution.save()
        print(f'[Execution]\'s id:{execution.pk} status changed to [green]filemove_process')
    elif completed == True:
        execution.status = 'completed'
        execution.save()
        print(f'[Execution]\'s id:{execution.pk} status changed to [green]completed')
    else:
        pass

def update_execution_current(id,current):
    execute = Execution.objects.get(pk=id)
    execute.current = current
    execute.save()
    print(f'Current parsing is: {current}')


def get_channel_id(msg_id,channel_name):
    global channel_id
    try:
        channel = TgChannel.objects.filter(from_name=channel_name,message_id=msg_id)
        channel_id = channel.values_list('pk',flat=True)[0]
        if channel_id != None:
            return channel_id
    except:
        tg_group =  TgGroup.objects.filter(channel_name=channel_name,message_id=msg_id)
        try:
            channel_id = tg_group.values_list('tg_channel_id', flat=True)[0]
            return channel_id
        except:
            channel_id = None
            try:
                rpl_msg_id = tg_group.values_list('replied_message_id', flat=True)[0]
            except:
                rpl_msg_id = None
            if rpl_msg_id == None and channel_id == None:
                print(f'This is parent message {tg_group.values_list('message_id', flat=True)[0]} of {msg_id}')
            elif rpl_msg_id != None and channel_id == None:
                get_channel_id(msg_id=rpl_msg_id, channel_name=channel_name)
            else:
                print('new bugssssssssss!!!!!!!!!!!!!!!!!!')

    return  channel_id






def insert_or_get_channel(data_c):
    exist = 0
    new = 0
    for data in data_c.values():
        try:
            tg_channel = TgChannel.objects.get(**data)
            exist+=1
            print(f'[{data["text"]}] already exist with channel_id:{tg_channel.pk}')
        except TgChannel.DoesNotExist:
            channel = TgChannel.objects.create(**data)
            new +=1
            print(f'[{data["text"]}] saved to db with channel_id:{channel.pk} ')
    return exist,new

def insert_or_get_group(data_g):
    exist = 0
    new = 0
    ex_id = None
    for data in data_g.values():
        ex_id = data['execution_id']

        if data['replied_message_id'] !=None:
            try:
                data["tg_channel_id"] = get_channel_id(data['replied_message_id'],data['channel_name'])
            except:
                print('Channel id not found',data['message_details'], data['replied_message_details'])
                data['tg_channel_id'] = None
        try:
            tg_group = TgGroup.objects.get(**data)
            exist += 1
            print(f'[{data["content"]}] already exist with group_id:{tg_group.pk}')
        except TgGroup.DoesNotExist:
            tg_group = TgGroup.objects.create(**data)
            new += 1
            print(f'[{data["content"]}] saved to db with group_id:{tg_group.pk} ')
    return exist, new,ex_id

def get_all_execution_status_pk():
    execution = Execution.objects.values('pk','status','name')
    return natsort.os_sorted(list(execution))

def get_all_none_channel_id_from_group():
    groups = TgGroup.objects.values('pk','message_id','replied_message_id','execution_id').filter(replied_message_id__isnull=False)
    return natsort.os_sorted(list(groups))


def get_none_tgchannelid_and_rplid():
    groups = TgGroup.objects.values('pk', 'message_id', 'replied_message_id', 'execution_id').filter(
        replied_message_id__isnull=True,tg_channel_id__isnull=True)
    return natsort.os_sorted(list(groups))

def get_all_rpl_msg(msg_id):
    return TgGroup.objects.filter(replied_message_id=msg_id)