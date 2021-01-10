"""
@Author: Jonescyna@gmail.com
@Created: 2021/1/10
"""
import requests
import time
from datetime import datetime, timezone, timedelta
from lxml import etree

url = 'https://covid19.who.int/table'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
# resp = requests.get(url, headers=headers).text
# doc = etree.HTML(resp)
# csv_path = doc.xpath('//a[contains(@href,"csv")]/@href')[0]
# published = doc.xpath('//a[contains(@href,"csv")]/@download')[0].split(' ')
# WHO COVID-19 global table data January 9th 2021 at 1.15.59 PM.csv
# print(published)


def transform_sequence(day):
    # 日期的天数的序数词转换
    sequence = '第1 first 第2 second 第3 third 第4 fourth 第5 fifth 第6 sixth 第7 seventh 第8 eighth 第9 ninth 第10 tenth 第11 eleventh 第12 twelfth 第13 thirteenth 第14 fourteenth 第15 fifteenth 第16 sixteenth 第17 seventeenth 第18 eighteenth 第19 nineteenth 第20 twentieth 第30 thirtieth 第31 thirty-first'
    sequence_map = {}
    for i in sequence.split('第'):
        if i:
            j = i.strip()
            head = j[:2].strip(' ')
            tail = j[-2:]
            sequence_map[head + tail] = int(head)
    return sequence_map[day]


def transform_timezone(file_name):
    # WHO COVID-19 global table data January 9th 2021 at 1.15.59 PM.csv
    # 时区转换
    spilt_list = file_name.split(' ')[5:]
    month = time.strptime(spilt_list[0], '%B').tm_mon
    day = transform_sequence(spilt_list[1])
    morning_or_afternoon = spilt_list[-1].split('.')[0]
    date = spilt_list[-2].split('.')
    if morning_or_afternoon == 'PM':
        date[0] = int(date[0]) + 12
    else:
        pass
    year = int(spilt_list[2])
    utc_time = datetime(year=year, month=month, day=day, hour=date[0], minute=int(date[1]), second=int(date[2]))
    bejing_time = datetime(year=year, month=month, day=day, hour=date[0], minute=int(date[1]),
                           second=int(date[2])).replace(
        tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=+8)))
    # print(f'国际标准时间:' + utc_time.strftime('%Y-%m-%d %X'))
    # 时区转换
    # print("北京时间:" + bejing_time.strftime('%Y-%m-%d %X'))
    return bejing_time


if __name__ == '__main__':
    print(transform_timezone('WHO COVID-19 global table data January 9th 2021 at 1.15.59 PM.csv'))
