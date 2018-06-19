# -*- coding: utf-8 -*-
import scrapy
import re
import time

class ApiKuaishouSpider(scrapy.Spider):
    name = 'api_kuaishou'
    allowed_domains = ['api.gifshow.com']
    #start_urls = ['http://api.gifshow.com/']

    header = {
        "Host": "www.kuaishou.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9"}

    a = {
        "__NStokensig": "9fc46e8ca452bdfb4ecf8881dd1c9169c298f00baa46522a2b19fc11aeec8a0f",
        "client_key": "56c3713c",
        "country_code": "cn",
        "language": "zh-Hans-CN;q=1",
        "photoId": "5250071271100053032",
        "sig": "a21994961d4c788cf2af6b0484d9d77b",
        "token": "5d5746dd68a140708f6d98760ee93e62-978283427",
        "visitor": "978283427"
    }


    # def start_requests(self):
    #     yield scrapy.FormRequest(url='http://124.243.205.129/rest/n/user/downloadPhoto?appver=5.7.4.500&did_gt=1528339635862&did=7E77006C-11B2-4638-995E-80A5A40DF858&c=a&ver=5.7&ud=978283427&sys=ios11.4&mod=iPhone10%2C3&net=%E4%B8%AD%E5%9B%BD%E7%A7%BB%E5%8A%A8_5',
    #                              method='POST', formdata=self.a, headers=self.heaser, callback=self.parse)

    def start_requests(self):
        for i in range(20):
            yield scrapy.Request(
                url='https://www.kuaishou.com/photo/40300007/4717642340',
                headers=self.header,
                callback=self.parse, method='GET', dont_filter=True)


    def parse(self, response):
        if response.status == 200:
            print('请求成功')
            #print(str(response.body, encoding='utf-8'))
            _re = str(response.body, encoding='utf-8')
            print(_re)
            # if 'functionjump()'in _re:
            #     cookie = re.match(r'.*vardata={\'cookie\':"(.*?)",', _re).group(1)
            #     print('cookie为:'+cookie)
            #     uri = re.match(r'.*\'uri\':"(.*?)",', _re).group(1)
            #     print('uri为：'+uri)
            #     _a = {"cookie": "ksbv_sign_javascript="+cookie}
            #     self.header.update(_a)
            #     _b = uri+'?ksjs_sig'+str(round(time.time()*1000))
            #     if 'ksjs_sig' not in uri:
            #         yield scrapy.Request(url=_b, headers=self.header,
            #                              method='GET', dont_filter=True, callback=self.detail_parse)

        else:
            print('请求失败')
    def detail_parse(self, response):
        print('我在detail里')
        if response.status == 200:
            print('请求成功')
            #print(str(response.body, encoding='utf-8'))
            _re = str(response.body, encoding='utf-8')
            print(_re)
        pass
