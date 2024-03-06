from Telegram.tg_bot import send_error_msg


def hashtag_txt(dst_path,hashtag_name,tg_channel_id,hashtag):
    try:
        with open(f'{dst_path}/#{hashtag_name}.txt', 'w', encoding='utf=8') as file:
            file.write(f'#{hashtag}')
    except Exception as e:
        print(e)
        send_error_msg(error=e, group_id=tg_channel_id)