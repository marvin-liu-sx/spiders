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
    table = book.sheet_by_name('zhishi')
    row_count = table.nrows
    for row in range(1, row_count):
        trdata = table.row_values(row)
        if 'https://www.meipai.com/' in trdata[0]:
            a = re.findall(r'https://www.meipai.com/media/\d*', trdata[0])[0]
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
        channel_id = '知识类'
        #print('channel_id--------->'+channel_id)

        media_name = str(response.xpath("//h3[@class='detail-name pa']/a/text()").extract_first()).strip()
        #print('media_name--------->'+media_name)

        media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()
        #print('media_id----------->'+media_id)

        video_id = re.match(r'.*media/(\d+)', response.url).group(1)
        #print('video_id------------->'+video_id)

        video_title = response.xpath("//h1[@class='detail-description break']").extract_first()
        #print('video_title---------->'+video_title)

        count = response.xpath("//div[@class='detail-info pr']/div[@class='detail-location']").extract_first()
        count = str(count).replace(' ', '').replace('\n', '')
        _c = re.match(r'.*</i>(.*)</div>$', count).group(1)
        _co = re.findall(r'\d*', _c)
        _r = _co[0]+_co[2]
        if '万' in _c:
            play_count = int(_r)*1000
        else:
            play_count = int(_r)

        #print('video_count--------------->'+str(play_count))

        duration = str(response.xpath("//div[@class='mp-h5-player-layer-control-tool-time']/text()").extract_first()).replace(' / ', '')
        _d = re.findall(r'\d*', duration)
        video_duration = str(int(_d[0]) * 60 + int(_d[2]))
        #print('duration--------->' + video_duration)

        #print('video_url-------------->'+response.url)

        video_cover = str(response.xpath("//div[@id='detailVideo']/img/@src").extract_first()).replace('!thumb480', '')
        #print('video_cover--------------->'+video_cover)

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
        item['source'] = 4
        item['status'] = 0
        item['meta_data'] = None
        item['video_width'] = 500
        item['video_height'] = 500
        yield item







