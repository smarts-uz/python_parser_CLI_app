from django_orm.db.db_functions import get_all_none_channel_id_from_group, get_channel_id, update_channel_id, \
    change_status_execution


def main_empty_channel():
    found = 0
    notfound = 0
    empties = get_all_none_channel_id_from_group()
    print(f'Channel id\'s None count : {len(empties)}')
    for empty in empties:
        channel_id = get_channel_id(msg_id=empty['replied_message_id'],channel_name=empty['channel_name'])
        update_channel_id(pk=empty['pk'],channel_id=channel_id)
        if channel_id != None:
            found+=1
            print(f'id = {empty['pk']}\'s channel_id updated = {channel_id} ')
        else:
            notfound+=1
            print(f' {empty['pk']} Channel id not found')
        change_status_execution(id=empty['execution_id'], parsing_ok=True)
    print(f'Channel id found: {found}')
    print(f'Channel id not found: {notfound}')