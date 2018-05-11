# -*- coding: utf-8 -*-
import scrapy
import xlrd
from scrapy.http import Request
import base64
import re
from ..items import MiaoPaiItem

data_arr = []

with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
    table = book.sheet_by_name('zhishi')
    row_count = table.nrows
    for row in range(1, row_count):
        trdata = table.row_values(row)
        if 'http://www.meipai.com/' in trdata[0]:
            data_arr.append(trdata[0])


class MeipaiSpider(scrapy.Spider):
    name = 'meipai'
    allowed_domains = ['www.meipai.com']

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', headers=self.default_header, encoding='utf-8', callback=self.parse)

    def parse(self, response):
        pass
