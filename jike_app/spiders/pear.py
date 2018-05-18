# -*- coding: utf-8 -*-
import scrapy
import xlrd
from scrapy.http import Request
import base64
import re
from ..items import MiaoPaiItem
import time
import random
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

data_arr = ['http://www.pearvideo.com/video_1337384', 'http://www.pearvideo.com/video_1339500',
            'http://www.pearvideo.com/video_1337407']

# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
#     table = book.sheet_by_name('zhishi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'http://www.pearvideo.com/' in trdata[0]:
#             data_arr.append(trdata[0])


class PearSpider(scrapy.Spider):

    # def __init__(self):
    #     dispatcher.connect(self.handles_spider_err, signals.spider_error)
    #
    # def handles_spider_err(self, spider, reason):
    #     print('reason----------->'+ reason)


    name = 'pear'
    allowed_domains = ['www.pearvideo.com']
    # start_urls = ['http://www.pearvideo.com/']

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', headers=self.default_header, encoding='utf-8', callback=self.parse)

    def parse(self, response):
        if response.status != 200:
            print(response.url)
        else:
            #print('video_url--------------->'+str(response.url))
            channel_id = '知识类'
            #print('channel_id--------------->' + channel_id)

            _s = random.sample([random.randint(1, 100000000000)], 1)
            _t = int(round(time.time() * 1000))
            i_id = _s[0] + _t
            #print('i_id------------------>' + str(i_id))

            _name = response.xpath(".//div[@class='col-name']/i[@class='col-icon fl']/img/@alt").extract_first()
            if _name:
                media_name = _name
            else:
                media_name = '暂无'
            #print('media_name------------->'+str(media_name))

            media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
            #print('media_id----------------->'+str(media_id))

            video_id = re.match(r'.*http://www.pearvideo.com/(.*)', response.url).group(1)
            #print('video_id-------------->'+str(video_id))

            _title = response.xpath(".//h1[@class='video-tt']/text()").extract_first()
            if _title:
                video_title = str(_title).replace('\n', '').strip()
            else:
                video_title = '暂无'
            #print('video_title-------------->'+str(video_title))

            _p = response.xpath(".//div[@class='fav']/text()").extract_first()
            if _p:
                play_count = int(_p)
            else:
                play_count = 0
            #print('play_count---------------->'+str(play_count))

            _r = response.xpath(".//div[@class='img prism-player play']/video/@src").extract_first()
            if _r:
                play_url = _r
            else:
                play_url = '暂无'
            #print('play_url------------->'+str(play_url))

            _d1 = response.xpath(".//span[@class='duration']/text()").extract_first()
            if _d1:
                _d2 = re.findall(r'\d+', _d1)
                video_duration = int(_d2[0])*60+int(_d2[1])
            else:
                video_duration = 0
            #print('video_duration------------->'+str(video_duration))

            _c = response.xpath(".//div[@id='poster']/img[@class='img']/@src").extract_first()
            if _c:
                video_cover = _c
            else:
                video_cover = '暂无'
            #print('video_cover------------->'+str(video_cover))
    ########################################################################################################################
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
            item['source'] = 7
            item['status'] = 0
            item['meta_data'] = None
            item['i_id'] = i_id
            item['video_width'] = 640
            item['video_height'] = 360
            item['play_url'] = play_url
            yield item