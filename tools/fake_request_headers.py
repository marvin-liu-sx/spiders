# _*_coding:utf-8_*_
# Time : 2018/4/20 11:20
# User : zc-yy
# Email: zhangcong2@yy.com


"""Documentation comments"""
from random import randint
import uuid
import time
from urllib import parse


class randomHeaders(object):
    headers_list = []
    url_decode = ''

    def __init__(self):
        pass

    def set_header(self):
        for i in range(100):
            b_time = str(int(round(time.time() * 1000)))
            u_id1 = str(uuid.uuid4())
            u_id2 = str(uuid.uuid4())
            u_id3 = str(uuid.uuid4())
            u_id4 = str(uuid.uuid4())
            u_id5 = str(uuid.uuid4())
            self.url_decode = 'jike:config:searchPlaceholderLastInfo=' + b_time + '#2; jike:sess=eyJfdWlkIjoiNWFkNTg5MGM3ZWM3Y2MwMDE3NGVkZWVjIiwiX3Nlc3Npb25Ub2tlbiI6IjVMV3JlZUhlYTY4Vko5eUdZTlJOMDRETDIifQ==; jike:sess.sig=8HhiEx138ou3h2euBQiYXU_l-3g; jike:feed:latestFeedItemId=' + u_id1 + '; jike:feed:latestNormalMessageId=' + u_id2 + '; jike:feed:noContentPullCount=0; sensorsdata2015jssdkcross={"distinct_id":"' + u_id3 + '","$device_id":"' + u_id4 + '","props":{"$latest_referrer":"","$latest_referrer_host":""},"first_id":"' + u_id5 + '"}'
            re_header = {
                'Host': 'app.jike.ruguoapp.com',
                'Accept': '*/*',
                'App-BuildNo': '1100',
                'App-Version': '4.3.2',
                'BundleID': 'com.ruguoapp.jike',
                'OS': 'ios',
                'Accept-Language': 'zh-cn',
                'Accept-Encoding': 'br,gzip,deflate',
                'Content-Type': 'application/json',
                'Manufacturer': 'Apple',
                'User-Agent': '%E5%8D%B3%E5%88%BB/1100 CFNetwork/897.15 Darwin/17.5.0',
                'Connection': 'keep-alive',
                'Cookie': parse.quote(self.url_decode)
            }
            self.headers_list.append(re_header)
        return self.headers_list

    def get_header(self):
        self.set_header()
        return self.headers_list[randint(0, len(self.headers_list))]


if __name__ == '__main__':
    a = randomHeaders()
    print(a.get_header())
