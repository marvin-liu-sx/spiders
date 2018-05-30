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
#     table = book.sheet_by_name('tiyuyouxi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'https://m.365yg.com/' in trdata[0]:
#             re_data = re.match(r'(.*iid=)', trdata[0]).group(1).replace('/?iid=', '')
#             data_arr.append(re_data)
# print(data_arr)
# print(len(data_arr))


class SunshineSpider(scrapy.Spider):
    name = 'sunshine'
    allowed_domains = ['www.365yg.com']
    # start_urls = ['http://www.365yg.com/']

    # default_header = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Cache-Control": "max-age=0",
    #     "Connection": "keep-alive",
    #     "Cookie": "UM_distinctid=1638ab4bfb6127-07124df5923546-7315394b-1fa400-1638ab4bfb74aa; _ga=GA1.2.1377771956.1527040491; _gid=GA1.2.1090707533.1527142361; CNZZDATA1262382642=635589111-1527035561-%7C1527149623",
    #     "Host": "www.365yg.com",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36"
    # }

    def start_requests(self):
        for i in data_arr:
            yield Request(url=i, method='GET', encoding='utf-8', meta={'key': str(i)}, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')

            _s = random.sample([random.randint(1, 100000000000)], 1)
            _t = int(round(time.time() * 1000))
            i_id = _s[0] + _t

            channel_id = '知识类'

            if response.xpath(".//span[@class='name']/text()").extract_first():
                media_name = response.xpath(".//span[@class='name']/text()").extract_first()
            else:
                media_name = '暂无'

            media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()

            video_id = re.match(r'.*group/(\d+)', response.meta['key']).group(1)

            if response.xpath(".//div[@class='abstract']/h2[@class='title']/text()").extract_first():
                video_title = response.xpath(".//div[@class='abstract']/h2[@class='title']/text()").extract_first()
            else:
                video_title = '暂无'

            if response.xpath(".//span[@class='num']/em/text()").extract_first():
                _play_count = response.xpath(".//span[@class='num']/em/text()").extract_first()
                _play_count2 = re.match(r'(\d+)', _play_count).group(1)
                if '万' in _play_count:
                    play_count = _play_count2*10000
                else:
                    play_count = _play_count2
            else:
                play_count = 0

            if response.xpath(".//video[@id='vjs_video_3_html5_api']/@src").extract():
                play_url = response.xpath(".//video[@id='vjs_video_3_html5_api']/@src").extract()
            else:
                play_url = '暂无'

            if response.xpath(".//div[@class='vjs-duration-display']/text()").extract_first():
                _video_duration = response.xpath(".//div[@class='vjs-duration-display']/text()").extract_first()
                _video_duration2 = re.findall(r'\d*', _video_duration)
                video_duration = int(_video_duration2[0]*60)+int(_video_duration2[1])
            else:
                video_duration = 0



            item = MiaoPaiItem()
            item['i_id'] = i_id
            item['channel_id'] = channel_id
            item['media_name'] = media_name
            item['media_id'] = media_id
            #item['video_id'] = video_id
            item['video_title'] = video_title
            item['play_count'] = play_count
            item['video_url'] = response.meta['key']
            item['play_url'] = play_url
            item['video_duration'] = video_duration
            item['video_cover'] = '暂无'
            item['source'] = 14
            item['status'] = 0
            item['meta_data'] = None
            item['video_width'] = 660
            item['video_height'] = 375
            print(item)
        else:
            print('请求失败')
