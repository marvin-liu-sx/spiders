# -*- coding: utf-8 -*-
import scrapy
import json
import time
import uuid

class ApiPearSpider(scrapy.Spider):
    name = 'api_pear'
    allowed_domains = ['www.pearvideo.com']
    # start_urls = ['http://www.pearvideo.com/']

    post_header = {
        "Host": "app.pearvideo.com",
        "User-Agent": "LiVideoIOS / 4.2.4(iPhone;iOS11.3.1;Scale / 3.00)",
        "X-Channel-Code": "official",
        "Cookie": "JSESSIONID="+str(uuid.uuid4()).upper().replace('-', '')+";PEAR_UUID="+str(uuid.uuid4()).upper(),
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

    def start_requests(self):
        yield scrapy.FormRequest(url='http://app.pearvideo.com/clt/jsp/v4/content.jsp', formdata={"contId": "1335699"},
                                 headers=self.post_header, callback=self.parse)

    def parse(self, response):
        if response.status == 200:
            # data = json.loads(str(response.body, encoding='utf-8'))
            # print(type(data))
            print(str(response.body, encoding='utf-8'))
        else:
            print('失败')