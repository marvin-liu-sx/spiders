# -*- coding: utf-8 -*-
import scrapy
import json
import time
import random
import uuid
import re
from ..items import MiaoPaiItem

TOPIC = '测试'


class Safe:
    @staticmethod
    def bytes(s, default_value=b'') -> bytes:
        if isinstance(s, str):
            return s.encode('utf-8')
        elif isinstance(s, bytes):
            return s
        return default_value


class RandomUid(object):
    def __init__(self):
        pass

    def get_uid(self) -> str:
        return str(round(time.time() * 1000)) + str(random.randint(10000, 99999))


class RandomHeaders(object):
    def __init__(self):
        pass

    def get_postheader(self):
        post_header = {
            ":method": "POST",
            ":scheme": "https",
            ":path": "/v1/user/info.json",
            "Cookie": "fudid=" + str(uuid.uuid4()).upper().replace('-', '') + ";sessionId=" + str(
                uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '')[
                                                 2:10] + ";uid=" + RandomUid().get_uid(),
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "br, gzip, deflate",
            "user-agent": "KG_Video/2.2.3 (iPhone; iOS 11.3.1; Scale/3.00)",
            "accept-language": "zh-Hans-CN;q=1",
            "Connection": "keep-alive"
        }
        return post_header


class FormData(object):
    def __init__(self):
        pass

    def md5(self, s) -> str:
        import hashlib
        m = hashlib.md5()
        m.update(Safe.bytes(s))
        return m.hexdigest()

    def get_form(self, data) -> dict:
        form_data = {
            "_aKey": "ANDROID",
            "_dId": "Redmi+Note+4X",
            "_lang": "zh_CN",
            "_uId": "",
            "_nId": "1",
            "_pName": "tv.yixia.bobo",
            "_pcId": "xiaomi_market",
            "_t": str(round(time.time())),
            "_udid": str(uuid.uuid4()).upper().replace('-', ''),
            "_vApp": "8403",
            "_vName": "2.8.6",
            "_vOs": "7.0",
            "requestID": str(uuid.uuid4()).replace('-', ''),
            "requestRetryCount": "0"
        }
        form_data2 = dict(form_data)
        form_data2.update(data)
        tokens = []
        for k in sorted(list(form_data2.keys())):
            tokens.append(k)
            tokens.append(str(form_data2.get(k)))
        tokens.append("Cc$nceR6qGg5^Pdv%4@C")
        sig = self.md5("".join(tokens)).lower()
        form_data2['_sign'] = sig[2:22]
        # print(form_data2)
        return form_data2


class AuthorApiBoboSpider(scrapy.Spider):
    name = 'author_api_bobo'
    allowed_domains = ['api.bbobo.com']

    # start_urls = ['http://api.bbobo.com/']
    page = 1
    a = {"page": "1", "userId": "6363581257657453569"}  # page为1时才会返回nickName
    m_name = ''

    def start_requests(self):

        yield scrapy.FormRequest(url='https://api.bbobo.com/v1/user/info.json',
                                 headers=RandomHeaders().get_postheader(),
                                 method='POST', dont_filter=True, formdata=FormData().get_form(dict(self.a)),
                                 callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')
            json_data = json.loads(response.body, encoding='utf-8')
            if json_data['msg'] == 'ok':
                print(json.dumps(json_data))
                if self.page == 1:
                    if 'nickName' in json_data['data']['info']:
                        self.m_name = json_data['data']['info']['nickName']
                    else:
                        self.m_name = '暂无'
                else:
                    pass
                _results = json_data['data']['videos']
                if _results:
                    print('数据返回成功,个数为:%s个' % len(_results))
                    for i in _results:
                        _s = random.sample([random.randint(1, 100000000000)], 1)
                        _t = int(round(time.time() * 1000))
                        i_id = _s[0] + _t

                        channel_id = ''
                        topic = TOPIC
                        question_type = ''
                        media_name = self.m_name

                        if 'userId' in i:
                            media_id = i['userId']
                        else:
                            media_id = '暂无'

                        if 'title' in i:
                            video_title = i['title']
                        else:
                            video_title = '暂无'

                        if 'videoId' in i:
                            video_id = i['videoId']
                            video_url = 'https://m.doradoer.com/show/channel/' + i['videoId']
                        else:
                            video_id = '暂无'
                            video_url = '暂无'

                        if 'playNum' in i:
                            play_count = i['playNum']
                        else:
                            play_count = 0

                        play_url = ''

                        if 'duration' in i:
                            duration_list = re.findall(r'\d+', i['duration'])
                            duration = int(duration_list[0]) * 60 + int(duration_list[1])
                            video_duration = duration
                        else:
                            video_duration = 0

                        if 'logo' in i:
                            video_cover = i['logo']
                        elif '172x120' in i['logos']:
                            video_cover = i['logos']['172x120']
                        elif '580x326' in i['logos']:
                            video_cover = i['logos']['580x326']
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
                        item['source'] = 6
                        item['status'] = 0
                        item['meta_data'] = json.dumps(json_data, ensure_ascii=False)
                        item['video_width'] = 640
                        item['video_height'] = 360
                        # yield item
                        print(item)
                else:
                    pass
            else:
                print('数据返回失败')
            has_more = len(json_data['data']['videos'])
            if has_more > 0:
                print('Has-More-Data')
                self.page += 1
                self.a['page'] = str(self.page)
                yield scrapy.FormRequest(url='https://api.bbobo.com/v1/user/info.json',
                                         headers=RandomHeaders().get_postheader(),
                                         method='POST', dont_filter=True, formdata=FormData().get_form(dict(self.a)),
                                         callback=self.parse)
            else:
                print('No-More-Data')
        else:
            print('请求失败')
