# -*- coding: utf-8 -*-
import scrapy
import json
import time
import uuid
import random
from ..items import MiaoPaiItem

author_list = ['10117614', '10054243']


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


class AuthorApiPearSpider(scrapy.Spider):
    name = 'author_api_pear'
    allowed_domains = ['www.pearvideo.com']

    # start_urls = ['http://www.pearvideo.com/']

    def start_requests(self):
        for i in author_list:
            yield scrapy.FormRequest(url='http://app.pearvideo.com/clt/jsp/v4/userHome.jsp', formdata={'userId': i},
                                     headers=RandomHeader().get_header(), method='POST', callback=self.detail_parse)

    def detail_parse(self, response):
        if response.status == 200:
            json_data = json.loads(response.body, encoding='utf-8')
            #print(json.dumps(json_data))
            if json_data['dataList']:
                for i in json_data['dataList']:
                    _s = random.sample([random.randint(1, 100000000000)], 1)
                    _t = int(round(time.time() * 1000))
                    i_id = _s[0] + _t

                    channel_id = ''
                    topic = '美食'
                    question_type = ''

                    if i['contInfo']['userInfo']['nickname']:
                        media_name = i['contInfo']['userInfo']['nickname']
                    else:
                        media_name = '暂无'

                    if i['contInfo']['userInfo']['userId']:
                        media_id = i['contInfo']['userInfo']['userId']
                    else:
                        media_id = '暂无'

                    if i['contInfo']['name']:
                        video_title = i['contInfo']['name']
                    else:
                        video_title = '暂无'

                    if i['contInfo']['contId']:
                        video_id = i['contInfo']['contId']
                    else:
                        video_id = '暂无'

                    if i['contInfo']['praiseTimes']:
                        play_count = i['contInfo']['praiseTimes']
                    else:
                        play_count = 0

                    play_url = ''
                    video_duration = 0
                    if i['contInfo']['videos']:
                        for v in i['contInfo']['videos']:
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

                    video_url = 'http://www.pearvideo.com/video_' + video_id

                    if i['contInfo']['pic']:
                        video_cover = i['contInfo']['pic']
                    else:
                        video_cover = '暂无'

                    item = MiaoPaiItem()
                    item['i_id'] = i_id
                    item['channel_id'] = channel_id
                    item['topic'] = topic
                    item['question_type'] = question_type
                    item['media_name'] = media_name
                    item['media_id'] = media_id
                    item['video_title'] = video_title
                    item['video_id'] = video_id
                    item['play_count'] = play_count
                    item['play_url'] = play_url
                    item['video_duration'] = video_duration
                    item['video_url'] = video_url
                    item['video_cover'] = video_cover
                    item['source'] = 11
                    item['status'] = 0
                    item['meta_data'] = json.dumps(json_data, ensure_ascii=False).replace('\'', '').replace('\\"', '')
                    item['video_width'] = 640
                    item['video_height'] = 360
                    yield item

            if json_data['nextUrl']:
                print('Has More Data')
                yield scrapy.Request(url=json_data['nextUrl'], method='GET', headers=RandomHeader().get_header(),
                                     callback=self.detail_parse, dont_filter=True)
            else:
                print('No More Data')
        else:
            print('请求失败')

    def parse(self, response):
        pass
