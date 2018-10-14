# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 下午 06:57
# @Author  : melon

from bs4 import BeautifulSoup

if __name__ == '__main__':

    html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class='title' name="dromouse"><b>The Dormouse's story</b></p>
    """

    soup = BeautifulSoup(html, 'lxml')
    # 格式化
    # print(soup.prettify())
    # print(soup.title.string)

    # 标签选择器
    # 选择元素
    # print(soup.title)
    # print(soup.head)
    # print(soup.p)
    # 获取属性的值
    # print(soup.p.attrs['name'])
    # print(soup.p['name'])
    # 获取内容
    # print(soup.p.string)
    # 嵌套选择
    # print(soup.head.title)
    # 获取子节点和子孙节点
    # print(soup.head.content)
    # print(soup.head.children)
    # print(soup.head.descendants)
    # 获取父节点和祖先节点
    # print(soup.p.parent)
    # print(soup.p.parents)
    # 获取兄弟节点

    # 标签选择器
    # print(soup.find_all('ul')[0])

    # CSS选择器
    print(soup.select('.clas'))