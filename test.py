import numpy as np
import csv


with open('C:/Users/jonescy/OneDrive/文档/PycharmProjects/Learning_python/Library/json or csv/itbook.csv', 'r', encoding='utf-8') as fr, \
        open('./Libary/numpy/test.csv', 'w', encoding='utf-8') as fd:
    for text in fr.readlines():
        if text.split():
            fd.write(text)
    print('输出成功....')
