''''
Test
first = "05.10.2021 10:10:08"
sec = "20.07.2023 16:49:33 UTC+05:00"
right_version = "2023-11-18 10:30:00"
'''
import datetime


def correct_time_data(data):
    first = data.split(' ')
    second = '-'.join(first[0].split('.')[::-1])
    result = f'{second} {first[1]}'
    return result


def year_converter(x):
    year = x[0:4]
    return year


# dt = datetime.datetime(2021, 10, 14, 1, 53, 14)
def correct_data_title(dt):
    formatted_date = dt.strftime("%Y-%m-%d %H:%M:%S")
    year = formatted_date[0:4]
    return year



# ===========================================================================
# "\\192.168.1.236\Exports\SmartTech Learning Group\2022\2022-4\messages.html"
# "\\192.168.1.236\Exports\Internal Teamviewer\2023-08-08\messages.html"
# "\\192.168.1.236\Exports\Envato Learning Group\2022-10-23\messages.html"
# ===========================================================================
# video_files/Using Flutter Cache managers.mp4
# files/oee.chm
# photos/photo_195@11-08-2022_22-00-34.jpg
# voice_messages/audio_214@26-08-2022_21-27-24.ogg
# "\\192.168.1.236\Exports\SmartTech Learning Group\2022\2022-4\files\5_0.zip"
# "\\192.168.1.236\Exports\Envato Learning Group\2023-08-10\photos\photo_16@11-11-2022_15-35-28.jpg"


a = 'photos/photo_16@11-11-2022_15-35-28.jpg'
b = r"\\192.168.1.236\Exports\Envato Learning Group\2023-08-10\messages10.html"


def get_file_path(content, mhtml_path, main_folder_name):
    correct_mhtml_path = mhtml_path.split('\\')
    correct_mhtml_path[-1] = content
    result_list = []
    if main_folder_name in correct_mhtml_path:
        break_point = correct_mhtml_path.index(main_folder_name)
        for i in range(break_point, len(correct_mhtml_path)):
            result_list.append(correct_mhtml_path[i])
    result = '\\'.join(result_list)
    return result
# get_file_path(a, b, 'Envato Learning Group')



