# -*- coding: utf-8 -*-
# @Time    : 2018/10/14 下午 10:06
# @Author  : melon

from selenium import webdriver
import time

'''selenium使用'''

if __name__ == '__main__':

    # 声明浏览器对象
    browser = webdriver.Chrome()
    # browser = webdriver.Firefox()

    # 访问页面
    browser.get("https://www.taobao.com")
    # print(browser.page_source)

    # 查找单个元素
    # find_element_by_name
    # find_element_by_xpath
    # find_element_by_partial_link_text
    # find_element_by_tag_name
    # find_element_by_class_name
    # find_element_by_css_selector

    # 元素交互操作
    # input = browser.find_element_by_id('q')
    # input.send_keys('iphone')
    # time.sleep(2)
    # input.clear()
    # input.send_keys('ipad')
    # button = browser.find_element_by_class_name('btn-search')
    # button.click()

    # 执行javascript
    browser.execute_script('alert("Hello")')

    # browser.close()
