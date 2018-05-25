# -*- coding: utf-8 -*-
import scrapy
import json
import time
import uuid
import random
import re
import base64
import xlrd
from ..items import MiaoPaiItem

data_arr = []

# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\2.xlsx') as book:
#     table = book.sheet_by_name('yulemingxing')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'https://www.bilibili.com/' in trdata[0]:
#             re_data = re.match(r'.*video/av(\d*)', trdata[0]).group(1)
#             data_arr.append(re_data)
#         elif 'http://www.bilibili.com/' in trdata[0]:
#             re_data = re.match(r'.*video/av(\d*)', trdata[0]).group(1)
#             data_arr.append(re_data)
#
# print(data_arr)
# print(len(data_arr))


class RandomHeader(object):
    def __init__(self):
        pass

    def get_header(self):
        post_header = {
            "Host": "app.bilibili.com",
            "Accept": "*/*",
            "Cookie": "buvid3=B2AA4510-D13D-4E55-9D39-0DF6E567366F14583infoc; finger=50e304e7; LIVE_BUVID=AUTO5115258816686773",
            "Connection": "keep-alive",
            "Display-ID": "1134402fc290d710313b9db99e310eed-1527077438",
            "Accept-Encoding": "gzip",
            "Accept-Language": "zh-cn",
            "User-Agent": "bili-universal/6680 CFNetwork/897.15 Darwin/17.5.0",
            "Buvid": "1134402fc290d710313b9db99e310eed",
            "Search-Track-ID": ""
        }
        return post_header


class ApiBiliSpider(scrapy.Spider):
    name = 'api_bili'
    allowed_domains = ['www.bilibili.com']

    # start_urls = ['http://www.bilibili.com/']

    def start_requests(self):
        yield scrapy.Request(url='https://app.bilibili.com/x/v2/view?actionKey=appkey'
                                 '&ad_extra=25539CAD5A3A25B848BFE0BBB4A384B6FA31DD57E9A866EDF1CF3C348BABFC34DBB4248F112B'
                                 '5EC0AF664453AE3BF344C0E118671D37C4C974DE2E1C4ABAFE26F0921F48484817290CA5919EAC8642BB14'
                                 '69417C37D265D46652D9F7D7B1D863E1FD4218FE9B974DF1D2AC2B7B746E61D9ED63B3155B80BD9A6B5D0F'
                                 'BAAAFE7EC0CB4DA052BB2407CEC843211FF7A8B6865668C3867BE7CB333AE1EB45ECFEE5D1B6D756257532'
                                 '535ABFE81DE5A0C9507B2A283BFE23FD4026EF7BA040813E5D2CB8BA7ADFE15A5B9F9DCF4854B8CD584F32'
                                 '23D1D653E420B29B6E0B3A266CB56AA6A13F81DD40C315FF149D73D575BC08FE77FEA319BB51C3F9649A5C'
                                 'AFE9CB0D838794CEFE309245B0DFD87EA73B19A615BDF49F4AEAC1615F307E36F60B9E59CAF4D5C37438A8'
                                 '019AD2FC66D595C0B29C09A67AD139B555D59690EF973D8D2F9708ED9A9BD0652836B91DC5B04CAF9B62B5'
                                 '0E208A4A49E30280905D24E762F76EDA0A1A92DE3A0A81702ED10D736C4F51F2BAE9229342A03ACF8D2573'
                                 '18788950409937A0F9EA16F74930DC20CE9D039DCE47AFE2AF3ED8BC83FA5887CE41558F43CD764EBF50C6'
                                 '10E125AC7324574CAA860E94C3AB2326554BDE54C75CECB70D1810FBC9053B07697C8815E1A8344C802826'
                                 '03BED24C701B648F20462F47B71D3AF7A33310FE1ED44941A1F63F7CFF244AADC72023EFF56A7AE3E3E094'
                                 'BFCA67B516F120C108D36F1569EEDE5854F0974FEC00FF9BD558F56DD99EA7AB1FCD64A769A4774605EEE9'
                                 '39CEC8346713'
                                 '&aid=23328041'
                                 '&appkey=27eb53fc9058f8c3'
                                 '&build=6680'
                                 '&device=phone'
                                 '&from=64'
                                 '&mobi_app=iphone'
                                 '&platform=ios'
                                 '&sign=6aa5092c78f9b61b1bacfe17989f6ec5'
                                 '&trackid='
                                 '&ts=1527077456', method='GET', headers=RandomHeader().get_header(), callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print(str(response.body, encoding='utf-8'))
            print('请求成功')
            data = json.loads(str(response.body, encoding='utf-8'))
            print(data)