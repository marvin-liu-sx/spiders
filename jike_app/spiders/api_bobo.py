# -*- coding: utf-8 -*-
import scrapy
import json
import time
import random
import uuid
import re
from ..items import MiaoPaiItem


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
            ":path": "/v1/video/play.json",
            ":authority": "api.bbobo.com",
            "Cookie": "fudid=" + str(uuid.uuid4()).upper().replace('-', '') + ";sessionId=" + str(
                uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '')[
                                                 2:10] + ";uid=" + RandomUid().get_uid(),
            "accept": "*/*",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "br, gzip, deflate",
            "user-agent": "Dalvik/2.1.0 (Linux; U; Android 7.0; Redmi Note 4X MIUI/V9.5.1.0.NCFCNFA)",
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


class ApiBoboSpider(scrapy.Spider):
    name = 'api_bobo'
    allowed_domains = ['api.bbobo.com']

    # start_urls = ['http://api.bbobo.com/']
    a = {"videoId": "6408529292006787073"}

    def start_requests(self):

        yield scrapy.FormRequest(url='https://api.bbobo.com/v1/video/play.json',
                                 headers=RandomHeaders().get_postheader(),
                                 method='POST', dont_filter=True, formdata=FormData().get_form(dict(self.a)),
                                 callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            print('请求成功')
            json_data = json.loads(response.body, encoding='utf-8')
            if 'msg' in json_data and json_data['msg'] == 'ok':
                print('数据返回成功')
                print(json.dumps(json_data))
            else:
                print('数据返回失败')
        else:
            print('请求失败')