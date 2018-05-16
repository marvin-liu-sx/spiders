# -*- coding: utf-8 -*-
import scrapy

import xlrd
from scrapy.http import Request
import base64
import re
from ..items import MiaoPaiItem
import time
import random

data_arr = []

with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
    table = book.sheet_by_name('qita')
    row_count = table.nrows
    for row in range(1, row_count):
        trdata = table.row_values(row)
        if 'https://weibo.com/tv/v/' in trdata[0]:
            a = re.findall(r'https://weibo.com/tv/v/.*', trdata[0])[0]
            data_arr.append(a)


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    # start_urls = ['http://weibo.com/']

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', headers=self.default_header, encoding='utf-8', callback=self.parse)

    def parse(self, response):

        channel_id = '体育游戏'
        print('channel_id--------------->' + channel_id)

        _s = random.sample([random.randint(1, 100000000000)], 1)
        _t = int(round(time.time() * 1000))
        i_id = _s[0] + _t
        print('i_id------------------>' + str(i_id))

        _name = response.xpath(".//span[@class='W_f14 L_autocut bot_name W_fl']/text()").extract_first()
        if _name:
            media_name = _name
        else:
            media_name = '暂无'
        print('media_name-------------->' + media_name)

        media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
        print('media_id------------------>' + media_id)

        _id = re.match(r'.*v/(.*)', response.url).group(1)
        if _id:
            video_id = _id
        else:
            video_id = '暂无'
        print('video_id--------------->' + video_id)

        _title = response.xpath(".//div[@class='info_txt W_f14']/text()").extract_first()
        if _title:
            video_title = _title
        else:
            video_title = '暂无'
        print('video_title------------->' + video_title)

        _d1 = response.xpath(
            ".//div[@class='weibo_player_fa']/div[@node-type='common_video_player']/@action-data").extract_first()
        _d2 = re.match(r'.*play_count=(.*)&duration', _d1).group(1)
        if _d2:
            _d3 = re.findall(r'\d+', _d2)[0]
            print('_d2------------->' + _d2)
            print('_d3------------->' + _d3)
            if '万' in _d2:
                play_count = int(_d3) * 10000
            else:
                play_count = int(_d3)
        else:
            play_count = 0
        print('play_count--------------->' + str(play_count))

        video_url = response.url
        print('video_url-------------->' + str(video_url))

        _p = response.xpath(".//div[@class='con-2 hv-pos hv-center']/video/@src").extract_first()
        play_url = re.match(r'.*//(.*)', _p).group(1)
        print('play_url------------->' + str(play_url))
