import json



from Json.filter_json import filter_message
from Json.json_search import json_search
from django_orm.db.db_functions import insert_or_get_channel, insert_or_get_group, get_execution_data_from_id, \
    change_status_execution
from django_orm.db.db_save import insert_data_to_db
from parsing.file_func.check_file_absent import check_file_absent


def json_extract(execution_id):
    execution = get_execution_data_from_id(ex_id=execution_id)
    json_list = json_search(path=execution.path)
    print(execution.path)
    try:
        for js in json_list:
            with open(f"{js}", mode='r', encoding='utf-8') as f:
                data = json.load(f)
                data_data = filter_message(datas=data['messages'], path=execution.path, channel_name=execution.name,
                                           execution_id=execution_id)
                for channel_data in data_data[0]:
                    insert_or_get_channel(channel_data)
                for group_data in data_data[1]:
                    insert_or_get_group(group_data)

        change_status_execution(id=execution_id, parsing_ok=True)
    except:
        change_status_execution(id=execution_id, parsing_process=True)




# json_extract('866')



# execution = get_execution_data_from_id(ex_id=862)
# print(execution.path)

