# -*- coding: utf-8 -*-
# @Time    : 2018/8/6 上午 05:55
# @Author  : melon

"""垃圾邮件过滤之数据清洗"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import time
import jieba
import os


# 索引文件读取
def read_index_file(file_path):
    # 垃圾邮件用1表示，正常邮件用0表示
    type_dict = {"spam": "1", "ham": "0"}
    index_file = open(file_path)
    index_dict = {}
    try:
        for line in index_file:
            arr = line.split(" ")
            if len(arr) == 2:
                key, value = arr
            # 添加到字段中
            value = value.replace("../data", "").replace("\n", "")
            index_dict[value] = type_dict[key.lower()]
    finally:
        index_file.close()

    return index_dict


# 单个邮件的文件内容数据读取
def read_file(file_path):
    file = open(file_path, "r", encoding="gb2312", errors='ignore')
    content_dict = {}

    try:
        is_content = False
        for line in file:
            line = line.strip()
            if line.startswith("From:"):
                content_dict['from'] = line[5:]
            elif line.startswith("To:"):
                content_dict['to'] = line[3:]
            elif line.startswith("Date:"):
                content_dict['date'] = line[5:]
            elif not line:
                # 如果当前行为空，那么表示接下来的数据应该是邮件的主体内容
                is_content = True

            # 处理邮件内容
            if is_content:
                if 'content' in content_dict:
                    # 如果不是第一行的邮件主题内容，那么直接累加
                    content_dict['content'] += line
                else:
                    # 如果是邮件的第一行内容，那么直接添加
                    content_dict['content'] = line
    finally:
        file.close()

    return content_dict

# 邮件数据处理
def process_file(file_path):
    content_dict = read_file(file_path)

    # 进行处理
    result_str = content_dict.get('from', 'unknown').replace(',', '').strip() + ","
    result_str += content_dict.get('to', 'unknown').replace(',', '').strip() + ","
    result_str += content_dict.get('date', 'unknown').replace(',', '').strip() + ","
    result_str += content_dict.get('content', 'unknown').replace(',', ' ').strip()
    return result_str

# 开始进行数据处理
# index_dict = read_index_file('../../datasets/full/index')
# list0 = os.listdir('../data/data')
# for l1 in list0:
#     l1_path = '../data/data/' + l1
#     print('开始处理文件夹:' + l1_path)
#     list1 = os.listdir(l1_path)
#
#     write_file_path = '../data/process01_' + l1
#     with  open(write_file_path, "w", encoding='utf-8') as writer:
#         for l2 in list1:
#             l2_path = l1_path + "/" + l2
#             # 得到具体的文件内容后，进行文件数据的读取
#             index_key = "/" + l1 + "/" + l2
#
#             if index_key in index_dict:
#                 # 读取数据
#                 content_str = process_file(l2_path)
#                 # 添加标签
#                 content_str += "," + index_dict[index_key] + "\n"
#                 # 进行数据输出
#                 writer.writelines(content_str)

if __name__ == "__main__":

    # 1.开始进行数据处理
    index_dict = read_index_file('../../datasets/index')

    # 2.数据处理
    listDir = os.listdir('../../datasets/mail')
    for list in listDir:
        write_file_path = "../../datasets/mail/processmail_" + list
        with  open(write_file_path, "w", encoding='utf-8') as writer:
            # 读取数据
            content_str = process_file(list)
            # 添加标签
            content_str += "," + index_dict[index_key] + "\n"
            # 数据输出
            writer.writelines(content_str)

    # print(index_dict)
