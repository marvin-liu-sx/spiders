# -*- coding: utf-8 -*-
import scrapy
import xlrd
from scrapy.http import Request
import base64
import re
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from ..items import MiaoPaiItem

data_arr = []


with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
    table = book.sheet_by_name('name')
    row_count = table.nrows
    for row in range(1, row_count):
        trdata = table.row_values(row)
        if 'http://www.miaopai.com/' in trdata[0]:
            data_arr.append(trdata[0])


class MiaopaiSpider(scrapy.Spider):
    name = 'miaopai'
    allowed_domains = ['www.miaopai.com']

    # start_urls = ['http://www.miaopai.com/']

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='F:/chromedriver.exe')
        super(MiaopaiSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        print('spider_closed')
        self.browser.quit()

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', meta={'key': i}, headers=self.default_header, encoding='utf-8',
                          callback=self.parse)

    def parse(self, response):
        if response:
            channel_id = '体育游戏'
            #print('channel_id------------>' + channel_id)
            media_name = response.xpath("//div[@class='personalAbout']/div[@class='personalData']/p[@class='personalDataN']/a/text()").extract()[0]
            media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
            #print('media_name------------>' + media_name)
            #print('media_id-------------->' + media_id)

            video_id = str(response.meta['key'][28:]).replace('__.htm', '')
            #print('video_id--------------->' + video_id)
            video_title = response.xpath("//div[@class='viedoAbout']/p/text()").extract()[0]
            #print('video_title------------->' + video_title)

            count = response.xpath("//span[@class='red']/text()").extract()[0]
            #print(count)
            re_list = re.findall(r'\d*', count)
            play_count = re_list[0] + re_list[2]
            if '万' in count:
                play_count = int(play_count) * 1000
            else:
                play_count = int(play_count)
            #print(play_count)

            duration = response.xpath("//div[@class='video-player']/div[@class='controls-wrap']/div[@class='controls']/div[@class='time']/b[@class='total']/text()").extract()[0]
            _d = re.findall(r'\d*', duration)
            video_duration = str(int(_d[0]) * 60 + int(_d[2]))
            #print('video_duration---------->' + video_duration)

            #print(response.url)

            video_cover = response.xpath("//div[@class='video']/div[@class='MIAOPAI_player']/div[@class='video-player']/video[@class='video']/@ poster").extract_first()
            #print(video_cover)

            width = response.xpath("//div[@class='video']/div[@class='MIAOPAI_player']/@ style").extract_first()
            video_width = re.findall(r'\d*', width)[6]
            #print(video_width)

            height = response.xpath("//div[@class='video']/div[@class='MIAOPAI_player']/div[@class='video-player']/@ style").extract_first()
            video_height = re.findall(r'\d*', height)[16]
            #print(video_height)



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
            item['source'] = 3
            item['status'] = 0
            item['meta_data'] = None
            item['video_width'] = video_width
            item['video_height'] = video_height
            yield item


















