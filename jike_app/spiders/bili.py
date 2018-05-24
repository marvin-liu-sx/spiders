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

# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\2.xlsx') as book:
#     table = book.sheet_by_name('yulemingxing')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'https://www.bilibili.com/' in trdata[0]:
#             a = re.findall(r'https://www.bilibili.com/video/av\d*', trdata[0])[0]
#             data_arr.append(a)
# print(data_arr)
# print(len(data_arr))

class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['www.bilibili.com']
    # start_urls = ['http://www.bilibili.com/']

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', headers=self.default_header, encoding='utf-8', callback=self.parse)

    def parse(self, response):
        channel_id = '娱乐明星'
        #print('channel_id--------->'+channel_id)

        media_name = response.xpath(".//div[@class='user clearfix']/a/text()").extract_first()
        #print('media_name-------->'+media_name)

        media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
        #print('media_id-------->'+media_id)

        video_id = re.match(r'.*/av(\d+)', response.url).group(1)
        #print('video_id----------->'+video_id)

        video_title = response.xpath(".//div[@id='viewbox_report']/h1/@title").extract_first()
        #print('video_title-------->'+video_title)

        count = response.xpath(".//div[@id='viewbox_report']/div[@class='number']/span[@class='v play']/@title").extract_first()
        #print('原始的count--------->', count)
        play_count = re.match(r'.*?(\d+)', count).group(1)
        #print('play_count--------->'+play_count)

        duration = response.xpath(".//span[@class='bilibili-player-video-time-total']/text()").extract_first()
        _d = re.findall(r'\d*', duration)
        video_duration = str(int(_d[0]) * 60 + int(_d[2]))
        #print('video_duration------------>'+video_duration)

        #print('video_url----------->'+response.url)

        #print('video_cover------------>'+'暂无')

        video_cover = response.xpath(".//head[@itemprop='video']/meta[@itemprop='image']/@content").extract_first()
        #print(video_cover)



        _s = random.sample([random.randint(1, 100000000000)], 1)
        _t = int(round(time.time() * 1000))
        i_id = _s[0] + _t

#######################################################################################################################
        item = MiaoPaiItem()

        item['channel_id'] = channel_id
        item['media_id'] = media_id
        item['media_name'] = media_name
        item['video_id'] = video_id
        item['video_title'] = video_title
        item['play_count'] = play_count
        item['play_url'] = 'changeable'
        item['video_duration'] = video_duration
        item['video_url'] = response.url
        item['video_cover'] = video_cover
        item['source'] = 9
        item['status'] = 0
        item['meta_data'] = None
        item['i_id'] = i_id
        item['video_width'] = 846
        item['video_height'] = 566
        yield item
        # B站的source为9