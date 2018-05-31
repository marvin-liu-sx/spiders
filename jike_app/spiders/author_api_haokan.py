# -*- coding: utf-8 -*-
import scrapy
import json
import time
import random
from ..items import MiaoPaiItem

appid_list = ['1558415107518709']
TOPIC = '好看测试'


class App(object):
    def __init__(self):
        pass

    def get_app_id(self):
        return str(appid_list[0])


class FakeUser(object):
    def __init__(self):
        pass

    __RANDOM_TOKENS = "0123456789ABCDEF"

    def random_str(self, length, radix=16) -> str:
        s = []
        for i in range(0, length):
            s.append(self.__RANDOM_TOKENS[random.randrange(1, min(16, radix))])
        return ''.join(s)

    def get_cuid(self):
        return self.random_str(32, radix=16).upper() + '|' + self.random_str(15, radix=10)

    def get_hid(self):
        return self.random_str(32, radix=16).upper()


class RandomHeader(object):
    def __init__(self):
        pass

    def get_header(self):
        post_header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 haokan/3.6.0.11 (Baidu; P1 7.0)/imoaiX_42_0.7_X4+etoN+imdeR/1014613h/9FF2CCC607BA386'
        }
        return post_header


class AhtuorApiHaokanSpider(scrapy.Spider):
    name = 'author_api_haokan'
    allowed_domains = ['sv.baidu.com']

    # start_urls = ['http://sv.baidu.com/']
    page = 1

    def start_requests(self):
        yield scrapy.FormRequest(
            url='https://sv.baidu.com/haokan/api?cuid=' + FakeUser().get_cuid() + '&hid=' + FakeUser().get_hid() + '&imei=0&imsi=0&network=1&os=android&osbranch=a0&apiv=3.6.0.0&appv=159&version=3.6.0.11',
            headers=RandomHeader().get_header(), method='POST',
            formdata={'baijia/listall': 'method=get&app_id=' + App().get_app_id() + '&_skip=' + str(
                self.page) + '&_limit=10'},
            callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')
            json_data = json.loads(response.body, encoding='utf-8')
            print(json.dumps(json_data))
            _results = json_data['baijia/listall']['data']['results']
            if _results:
                print('数据返回成功,个数为:%s个' % len(_results))
                for i in _results:
                    if i['type'] == 'video':
                        _s = random.sample([random.randint(1, 100000000000)], 1)
                        _t = int(round(time.time() * 1000))
                        i_id = _s[0] + _t

                        channel_id = ''
                        topic = TOPIC
                        question_type = ''

                        if i['content']['author']:
                            media_name = i['content']['author']
                        else:
                            media_name = '暂无'

                        if i['content']['authorid']:
                            media_id = i['content']['authorid']
                        else:
                            media_id = '暂无'
                        if i['content']['title']:
                            video_title = i['content']['title']
                        else:
                            video_title = '暂无'
                        if i['content']['vid']:
                            video_id = i['content']['vid']
                        else:
                            video_id = '暂无'
                        if i['content']['playcnt']:
                            play_count = i['content']['playcnt']
                        else:
                            play_count = 0
                        play_url = ''
                        if i['content']['video_list']:
                            if i['content']['video_list']['sd']:
                                play_url = i['content']['video_list']['sd']
                            elif i['content']['video_list']['hd']:
                                play_url = i['content']['video_list']['hd']
                            elif i['content']['video_list']['sc']:
                                play_url = i['content']['video_list']['sc']
                        else:
                            play_url = '暂无'

                        if i['content']['duration']:
                            video_duration = i['content']['duration']
                        else:
                            video_duration = 0

                        if i['content']['feed_id']:
                            video_url = 'https://haokan.baidu.com/videoui/page/videoland?context={"nid":"' + \
                                        i['content']['feed_id'] + '"}'
                        else:
                            video_url = '暂无'

                        if i['content']['cover_src']:
                            video_cover = i['content']['cover_src']
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
                        item['source'] = 5
                        item['status'] = 0
                        item['meta_data'] = json.dumps(json_data, ensure_ascii=False)
                        item['video_width'] = 672
                        item['video_height'] = 448
                        yield item
                        # print(item)
                    else:
                        pass
            else:
                print('数据返回失败')

            has_more = int(json_data['baijia/listall']['data']['has_more'])
            if has_more == 1:
                print('Has-More-Data')
                self.page += 1
                yield scrapy.FormRequest(
                    url='https://sv.baidu.com/haokan/api?cuid=' + FakeUser().get_cuid() + '&hid=' + FakeUser().get_hid() + '&imei=0&imsi=0&network=1&os=android&osbranch=a0&apiv=3.6.0.0&appv=159&version=3.6.0.11',
                    headers=RandomHeader().get_header(), method='POST',
                    formdata={'baijia/listall': 'method=get&app_id=' + App().get_app_id() + '&_skip=' + str(
                        self.page) + '&_limit=10'},
                    callback=self.parse)
            else:
                print('No-More-Data')
        else:
            print('请求失败')
