# _*_coding:utf-8_*_
# Time : 2018/4/20 11:20
# User : zc-yy
# Email: zhangcong2@yy.com


"""Documentation comments"""
from random import randint, sample
import string
import uuid
import time
import base64


class UidProvider(object):
    uid_list = []
    token_list = []

    def __init__(self):
        pass

    def get_uuid(self):
        for i in range(100):
            u_id = str(uuid.uuid4()).replace('-', '')
            fix_uid = u_id[:24]
            self.uid_list.append(fix_uid)
        return self.uid_list[randint(0, len(self.uid_list) - 1)]

    def get_token(self, num):
        fix_list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
        fix_str = sample(fix_list, int(num))
        new_str = ''
        last_str = new_str.join(fix_str)
        if last_str is not None:
            return last_str


class RandomHeaders(object):
    headers_list = []
    url_decode = ''

    def __init__(self):
        pass

    def set_header_list(self):
        for i in range(100):
            b_time = str(int(round(time.time() * 1000)))
            encode_dict = {"_uid": UidProvider().get_uuid(), "_sessionToken": UidProvider().get_token(25)}
            b_data = base64.b64encode(bytes(str(encode_dict), encoding='utf8'))
            s_data = str(b_data, encoding='utf8')
            cookie_data = 'jike:sess=' + s_data + '; jike:sess.sig=' + str(
                UidProvider().get_token(27)) + '; jike:config:searchPlaceholderLastInfo=' + b_time + '#1'
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
                'Cookie': cookie_data
            }
            self.headers_list.append(re_header)
        return self.headers_list

    def set_header(self):
        b_time = str(int(round(time.time() * 1000)))
        b_par = str([i for i in range(3)][randint(0, 2)])
        cookie_data = 'jike:config:searchPlaceholderLastInfo=' + b_time + '#' + b_par + ';' \
                                                                                        ' jike:sess=eyJfdWlkIjoiNWFlYTc0NmQ4YWRmZWYwMDE4MWUwMmJjIi' \
                                                                                        'wiX3Nlc3Npb25Ub2tlbiI6IkVPbTNTWWdkalN3VDJNNVFSWFRUZ3JxV1gifQ' \
                                                                                        '==; jike:sess.sig=PqUWhm5SYlTdHxiuIHtdYtWhQb4'
        re_header = {
            'Host': 'app.jike.ruguoapp.com',
            'Accept': '*/*',
            'App-BuildNo': '1107',
            'App-Version': '4.4.0',
            'BundleID': 'com.ruguoapp.jike',
            'OS': 'ios',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip,deflate',
            'Content-Type': 'application/json',
            'Manufacturer': 'Apple',
            'User-Agent': '%E5%8D%B3%E5%88%BB/1107 CFNetwork/897.15 Darwin/17.5.0',
            'Connection': 'keep-alive',
            'Cookie': cookie_data
        }
        return re_header

    def get_header(self):
        return self.set_header()


if __name__ == '__main__':
    a = RandomHeaders()
    print(a.get_header())
