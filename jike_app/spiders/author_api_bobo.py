# -*- coding: utf-8 -*-
import scrapy


class AuthorApiBoboSpider(scrapy.Spider):
    name = 'author_api_bobo'
    allowed_domains = ['api.bbobo.com']

    # start_urls = ['http://api.bbobo.com/']

    def parse(self, response):
        pass
