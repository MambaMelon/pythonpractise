# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    user_url = ''
    user_query = ''

    followers_url = ''
    followers_query = ''

    def start_requests(self):
        pass

    def parse_user(self):
        pass
    
    def parse_followers(self):
        pass
