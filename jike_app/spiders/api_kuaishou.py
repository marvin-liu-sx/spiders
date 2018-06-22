# -*- coding: utf-8 -*-
import scrapy
import re
import time
import xlrd

data_arr = []
with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\kuaishou.xlsx') as book:
    table = book.sheet_by_name('name')
    row_count = table.nrows
    for row in range(row_count):
        trdata = table.row_values(row)
        #_re = re.match(r'(.*?)\?', trdata[0]).group(1)
        data_arr.append(trdata[0])
print(data_arr)
print(len(data_arr))


class ApiKuaishouSpider(scrapy.Spider):
    name = 'api_kuaishou'
    allowed_domains = ['www.kuaishou.com']
    # start_urls = ['http://api.gifshow.com/']
    header = {
        #"Host": "www.kuaishou.com",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36",
        "Accept-Language": "zh-CN,zh;q=0.9"}

    # a = {
    #     "__NStokensig": "9fc46e8ca452bdfb4ecf8881dd1c9169c298f00baa46522a2b19fc11aeec8a0f",
    #     "client_key": "56c3713c",
    #     "country_code": "cn",
    #     "language": "zh-Hans-CN;q=1",
    #     "photoId": "5250071271100053032",
    #     "sig": "a21994961d4c788cf2af6b0484d9d77b",
    #     "token": "5d5746dd68a140708f6d98760ee93e62-978283427",
    #     "visitor": "978283427"
    # }

    def start_requests(self):
        for i in data_arr:
            yield scrapy.Request(
                url=i,
                method='GET',
                headers=self.header,
                callback=self.parse, dont_filter=True
            )

    def parse(self, response):
        if response.status != 404:
            #print('请求成功')
            html_body = str(response.body, encoding='utf-8').replace('\n', '').replace(' ', '')
            print(html_body)
            if 'functionjump()' in html_body:
                cookie = re.match(r'.*vardata={\'cookie\':"(.*?)",', html_body).group(1)
                print('cookie为:----------->' + cookie)
                uri = re.match(r'.*\'uri\':"(.*?)",', html_body).group(1)
                print('url为:-------->' + uri)
                new_dic = {"cookie": "ksbv_sign_javascript=" + cookie}
                self.header.update(new_dic)
                if '?ksjs_sig' not in uri:
                    new_url = uri + '?ksjs_sig' + str(round(time.time() * 1000))
                    yield scrapy.Request(
                        url=new_url,
                        method='GET',
                        headers=self.header,
                        dont_filter=True,
                        meta={'url': response.url},
                        callback=self.detail_parse
                    )
                else:
                    pass
            else:
                title = response.xpath('.//title/text()').extract_first()
                print('IN-Parse-Title'+title)
                if title == '快手，记录世界 记录你':
                    with open('kuaishou_filter.txt', 'a') as file:
                        file.write(response.url + '\n')

        else:
            print('请求失败')

    def detail_parse(self, response):
        print('IN--Detail')
        html_body = str(response.body, encoding='utf-8').replace('\n', '').replace(' ', '')
        print('IN-Detail-Parse------------->'+html_body)
        if response.status != 404:
            #print('请求成功')
            title = response.xpath('.//title/text()').extract_first()
            print('IN-Detail-Title------------------>'+title)
            if title == '快手，记录世界 记录你':
                with open('kuaishou_filter.txt', 'a') as file:
                    file.write(response.meta['url']+'\n')
            else:
                pass
        else:
            print('请求失败')
