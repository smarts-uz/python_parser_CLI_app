# def get_channel_id(msg_id):
#     global tg_channel_id
#     try:
#         tg_channel = TgChannel.objects.get(message_id=msg_id)
#         print('1', msg_id)
#         tg_channel_id = tg_channel.pk
#         print(f'tg_channel_id: {tg_channel_id}')
#         return tg_channel_id
#
#     except TgChannel.DoesNotExist:
#         try:
#             message = TgGroup.objects.get(message_id=msg_id)
#             print('2', msg_id)
#             rpl_msg_id = message.replied_message_id
#         except TgGroup.DoesNotExist:
#             rpl_msg_id = None
#             print(f'Tg_channel id and reply_message_id not found. Maybe parent message is not from Channel!!')
#         if rpl_msg_id != None:
#             try:
#                 tg_channel_id = TgGroup.objects.get(message_id=rpl_msg_id).tg_channel_id
#                 print('3', msg_id, rpl_msg_id)
#             except TgGroup.DoesNotExist:
#                 tg_channel_id = None
#             if tg_channel_id == None:
#                 get_channel_id(rpl_msg_id)
#                 print('4', msg_id)
#             else:
#                 print(f'tg_channel_id: {tg_channel_id}')
#                 return tg_channel_id



# def smth():
#     fname_list = search_html(path)
#     channel_content_list = []
#     group_content_list = []
#
#     for folder in fname_list:
#         f_path = folder_path(folder)
#         parsing = Pars(folder)
#         main_folder_name = parsing.parsing()[2]
#         ready_information = parsing.joined_messages()
#         channel_content = parsing.main_msg()
#         channel_content_list.append(channel_content)
#         group_content_list.append(ready_information)
#
#         save_to_execution(name=main_folder_name, path=f_path, status='in_process')
#
#     return [channel_content_list, group_content_list]
#
# def save_to_execution(name,path,status):
#     try:
#         execute = Execution.objects.get(path=path)
#         print('this path already exists!!')
#     except Execution.DoesNotExist:
#         execute = Execution.objects.create(
#             name = name,
#             path = path,
#             status = status
#         )
#         print(f'{path} saved to Execution table')
