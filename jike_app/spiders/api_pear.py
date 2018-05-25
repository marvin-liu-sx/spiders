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
#     table = book.sheet_by_name('zhishi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'http://www.pearvideo.com/' in trdata[0]:
#             re_data = re.match(r'.*?(\d+)', trdata[0]).group(1)
#             data_arr.append(re_data)
#
# print(data_arr)
# print(len(data_arr))


class RandomHeader(object):
    def __init__(self):
        pass

    def get_header(self):
        post_header = {
            "Host": "app.pearvideo.com",
            "User-Agent": "LiVideoIOS / 4.2.4(iPhone;iOS11.3.1;Scale / 3.00)",
            "X-Channel-Code": "official",
            "Cookie": "JSESSIONID=" + str(uuid.uuid4()).upper().replace('-', '') + ";PEAR_UUID=" + str(
                uuid.uuid4()).upper(),
            "X-Platform-Type": "1",
            "X-Serial-Num": str(round(time.time())),
            "X-Client-Agent": "APPLE_iPhone10,3_iOS11.3.1",
            "X-Client-Version": "4.2.4",
            "X-Platform-Version": "11.3.1",
            "Connection": "keep-alive",
            "Accept-Language": "zh-Hans-CN;q=1",
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate"
        }
        return post_header


class ApiPearSpider(scrapy.Spider):
    name = 'api_pear'
    allowed_domains = ['www.pearvideo.com']

    # start_urls = ['http://www.pearvideo.com/']

    def start_requests(self):
        for i in data_arr:
            yield scrapy.FormRequest(url='http://app.pearvideo.com/clt/jsp/v4/content.jsp',
                                     formdata={"contId": str(i)}, meta={"key": i},
                                     headers=RandomHeader().get_header(), callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')
            data = json.loads(str(response.body, encoding='utf-8'))
            print(json.dumps(data))
            if data['resultMsg'] == 'success':
                print('数据返回成功')

                _s = random.sample([random.randint(1, 100000000000)], 1)
                _t = int(round(time.time() * 1000))
                i_id = _s[0] + _t

                channel_id = '知识类'

                if data['content']['userInfo']['nickname']:
                    media_name = data['content']['userInfo']['nickname']
                else:
                    media_name = '暂无'
                media_id = base64.b64encode(str(media_name).encode('utf-8')).decode()

                video_id = response.meta['key']

                if data['content']['name']:
                    video_title = data['content']['name']
                else:
                    video_title = '暂无'

                if data['content']['praiseTimes']:
                    play_count = data['content']['praiseTimes']
                else:
                    play_count = 0
                play_url = ''
                video_duration = 0
                if data['content']['videos']:
                    for v in data['content']['videos']:
                        if v['tag'] == 'ld':
                            play_url = v['url']
                            video_duration = v['duration']
                        elif v['tag'] == 'sd':
                            play_url = v['url']
                            video_duration = v['duration']
                        elif v['tag'] == 'hd':
                            play_url = v['url']
                            video_duration = v['duration']
                        elif v['tag'] == 'fhd':
                            play_url = v['url']
                            video_duration = v['duration']
                else:
                    play_url = '暂无'
                    video_duration = 0

                if data['content']['pic']:
                    video_cover = data['content']['pic']
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
                item['video_url'] = 'http://www.pearvideo.com/video_' + str(response.meta['key'])
                item['play_url'] = play_url
                item['video_duration'] = video_duration
                item['video_cover'] = video_cover
                item['source'] = 11
                item['status'] = 0
                item['meta_data'] = json.dumps(data, ensure_ascii=False).replace('\'', '').replace('\\"', '')

                item['video_width'] = 640
                item['video_height'] = 360

                print(item)


            else:
                print('数据返回失败')
        else:
            print('请求失败')
        # 梨视频source为11
