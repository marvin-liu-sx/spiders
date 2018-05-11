# -*- coding: utf-8 -*-
import scrapy
import xlrd
from scrapy.http import Request
import base64
import re
from ..items import MiaoPaiItem

#data_arr = ['http://www.meipai.com/media/990160994']

data_arr = []

with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
    table = book.sheet_by_name('tiyuyouxi')
    row_count = table.nrows
    for row in range(1, row_count):
        trdata = table.row_values(row)
        if 'http://www.meipai.com/' in trdata[0]:
            a = re.findall(r'http://www.meipai.com/media/\d*', trdata[0])[0]
            data_arr.append(a)


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
        channel_id = '体育游戏'
        print('channel_id--------->'+channel_id)

        media_name = str(response.xpath("//h3[@class='detail-name pa']/a/text()").extract_first()).strip()
        print('media_name--------->'+media_name)

        media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
        print('media_id----------->'+media_id)

        # video_id = re.findall(r'^http://www.meipai.com/media/*?', response.url)
        # print(video_id)

        video_title = response.xpath("//h1[@class='detail-description break']").extract_first()
        print('video_title---------->'+video_title)

        count = response.xpath("//div[@class='detail-info pr']/div[@class='detail-location']").extract_first()
        # #play_count = re.findall(r'\d*', count)
        print('count------->'+count)

        duration = str(response.xpath("//div[@class='mp-h5-player-layer-control-tool-time']/text()").extract_first()).replace(' / ', '')
        _d = re.findall(r'\d*', duration)
        video_duration = str(int(_d[0]) * 60 + int(_d[2]))
        print('duration--------->' + video_duration)

        print('video_url-------------->'+response.url)

        video_cover = str(response.xpath("//div[@id='detailVideo']/img/@src").extract_first()).replace('!thumb480', '')
        print('video_cover--------------->'+video_cover)










