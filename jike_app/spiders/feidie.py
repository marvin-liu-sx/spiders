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
#     table = book.sheet_by_name('zhishi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'http://www.feidieshuo.com/' in trdata[0]:
#             data_arr.append(trdata[0])
# print(data_arr)
# print(len(data_arr))


class FeidieSpider(scrapy.Spider):
    name = 'feidie'
    allowed_domains = ['www.feidieshuo.com']
    # start_urls = ['http://www.feidieshuo.com/']

    default_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36'

    }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', headers=self.default_header, encoding='utf-8', callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')

            _s = random.sample([random.randint(1, 100000000000)], 1)
            _t = int(round(time.time() * 1000))
            i_id = _s[0] + _t

            channel_id = '知识类'

            media_name = '飞碟说'

            media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()

            video_id = re.match(r'.*?(\d+)', response.url).group(1)

            if response.xpath(".//div[@class='t-word-text']/h3/text()").extract_first():
                video_title = response.xpath(".//div[@class='t-word-text']/h3/text()").extract_first()
            else:
                video_title = '暂无'

            if response.xpath(".//span[@class='pull-left mr-1-5']/text()").extract_first():
                play_count = response.xpath(".//span[@class='pull-left mr-1-5']/text()").extract_first()
            else:
                play_count = 0

            if response.xpath(".//div[@id='player']/script/text()").extract_first():
                _paly_url = response.xpath(".//div[@id='player']/script/text()").extract_first()
                _paly_url2 = _paly_url.replace('\r', '').replace('\n', '').replace('\t', '').replace('\'', '"')
                _paly_url3 = re.match(r'.*(mp4.*.mp4)', _paly_url2).group(1)
                play_url = 'http://video.feidieshuo.com/' + _paly_url3
            else:
                play_url = '暂无'

            if response.xpath(".//script[@type='application/ld+json']/text()").extract_first():
                _cover = response.xpath(".//script[@type='application/ld+json']").extract_first()
                _cover2 = str(_cover).replace('\r', '').replace('\n', '').replace('\t', '').replace('\'', '').replace(
                    ' ', '')
                _cover3 = re.match(r'.*images":\["(.*"])', _cover2).group(1).replace('"]', '')
                video_cover = _cover3
            else:
                video_cover = '暂无'

            item = MiaoPaiItem()
            item['i_id'] = i_id
            item['channel_id'] = channel_id
            item['media_name'] = media_name
            item['media_id'] = media_id
            item['video_id'] = video_id
            item['video_title'] = video_title
            item['play_count'] = play_count
            item['video_url'] = response.url
            item['play_url'] = play_url
            item['video_duration'] = 0
            item['video_cover'] = video_cover
            item['source'] = 12
            item['status'] = 0
            item['meta_data'] = None
            item['video_width'] = 740
            item['video_height'] = 450
            yield item
            # 飞碟说 source 为12
        else:
            print('请求失败')
