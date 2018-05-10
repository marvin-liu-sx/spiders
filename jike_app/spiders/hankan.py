# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class HankanSpider(scrapy.Spider):
    name = 'hankan'
    allowed_domains = ['sv.baidu.com']
    #start_urls = ['https://sv.baidu.com/']

    def start_requests(self):

        pass


    def parse(self, response):
        pass
