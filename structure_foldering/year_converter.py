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


#  date(2021, 10, 15)
#  2021-10-15, or 2021-05, or 2021
def correct_time(dt):
    first = dt.split('-')
    if len(first) == 3:
        result = datetime.date(first[0], first[1], first[2])
    elif len(first) == 2:
        result = datetime.date()


a = datetime.datetime(2022, 9, 1, 14, 10, 59)
print(a)
