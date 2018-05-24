# -*- coding: utf-8 -*-
import scrapy

import xlrd
from scrapy.http import Request
import base64
import re
from ..items import MiaoPaiItem
import time
import random
from urllib import parse

data_arr = []

# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\2.xlsx') as book:
#     table = book.sheet_by_name('zhishi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'https://weibo.com/tv/v/' in trdata[0]:
#             a = re.findall(r'https://weibo.com/tv/v/.*', trdata[0])[0]
#             data_arr.append(a)
# print(data_arr)
# print(len(data_arr))

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

        channel_id = '知识类'
        #print('channel_id--------------->' + channel_id)

        _s = random.sample([random.randint(1, 100000000000)], 1)
        _t = int(round(time.time() * 1000))
        i_id = _s[0] + _t
        #print('i_id------------------>' + str(i_id))

        _name = response.xpath(".//span[@class='W_f14 L_autocut bot_name W_fl']/text()").extract_first()
        if _name:
            media_name = _name
        else:
            media_name = '暂无'
        #print('media_name-------------->' + media_name)

        media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
        #print('media_id------------------>' + media_id)

        _id = re.match(r'.*v/(.*)', response.url).group(1)
        if _id:
            video_id = _id
        else:
            video_id = '暂无'
        #print('video_id--------------->' + video_id)

        _title = response.xpath(".//div[@class='info_txt W_f14']/text()").extract_first()
        if _title:
            video_title = str(_title).strip().replace('\n', '').replace(' ', '').replace('’', '\'')
        else:
            video_title = '暂无'
        #print('video_title------------->' + video_title)

        _d1 = response.xpath(".//div[@class='weibo_player_fa']/div[@node-type='common_video_player']/@action-data").extract_first()
        _d2 = re.match(r'.*play_count=(.*)&duration', _d1).group(1)
        if _d2:
            _d3 = re.findall(r'\d+', _d2)[0]
            #print('_d2------------->' + _d2)
            #print('_d3------------->' + _d3)
            if '万' in _d2:
                play_count = int(_d3) * 10000
            else:
                play_count = int(_d3)
        else:
            play_count = random.randint(500, 1000)
        #print('play_count--------------->' + str(play_count))


        _duration = re.match(r'.*&duration=(\d+)', _d1).group(1)
        if _duration:
            video_duration = _duration
        else:
            video_duration = 0
        #print('video_duration------------->'+str(video_duration))

        _cover = re.match(r'.*cover_img=(.*)&card_height', _d1).group(1)
        if _cover:
            video_cover = parse.unquote(_cover)
        else:
            video_cover = 'NoData'
        #print('video_cover------------>'+str(video_cover))

        #video_url = response.url
        #print('video_url-------------->' + str(video_url))

        _width = re.match(r'.*&card_width=(\d+)', _d1).group(1)
        if _width:
            video_width = _width
        else:
            video_width = 0
        #print('video_width-------------->'+str(video_width))

        _heigth = re.match(r'.*&card_height=(\d+)', _d1).group(1)

        if _heigth:
            video_height = _heigth
        else:
            video_height = 0
        #print('video_height---------->'+str(video_height))

        #_p = response.xpath(".//div[@class='con-2 hv-pos hv-center']/video/@src").extract_first()
        # if _p:
        #     play_url = re.match(r'.*//(.*)', _p).group(1)
        # else:
        #     play_url = 'ch'
        #print('play_url------------->' + str(play_url))

#######################################################################################################################
        item = MiaoPaiItem()
        item['channel_id'] = channel_id
        item['media_id'] = media_id
        item['media_name'] = media_name
        item['video_id'] = video_id
        item['video_title'] = video_title
        item['play_count'] = play_count
        item['video_duration'] = video_duration
        item['video_url'] = response.url
        item['video_cover'] = video_cover
        item['source'] = 10
        item['status'] = 0
        item['meta_data'] = None
        item['i_id'] = i_id
        item['video_width'] = video_width
        item['video_height'] = video_height
        item['play_url'] = 'changeable'
        yield item