# -*- coding: utf-8 -*-
# @Time    : 2018/7/9 下午 09:59
# @Author  : melon

# 浅拷贝
names = ["小明", "小红", "小黑", "小黄", "小白"]
names2 = names.copy()
names[2] = "Lisi"

# extend().与append()有一定区别
l1 = [1, 2]
# [1, 2, '不', '得', '了']
l1.extend("不得了")
# [1, 2, '不', '得', '了', '不得了']
l1.extend(["不得了"])
print(l1)
