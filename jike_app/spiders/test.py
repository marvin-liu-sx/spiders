# _*_coding:utf-8_*_
# Time : 2018/4/19 14:01
# User : zc-yy
# Email: zhangcong2@yy.com


"""Documentation comments"""
import xlrd
# post_data = {'categoryAlias':'RECOMMENDATION'}
# post_data2 = '{"categoryAlias":"RECOMMENDATION"}'
# print(post_data)
# print(post_data2)
# print(str(post_data).replace('\'', '"'))

# class getLoadMoreKey(object):
#     """产出loadMoreKey参数"""
#
#     def __init__(self, max_limit):
#         self.max_limt = max_limit
#         self.n = 32
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max_limt:
#             self.n += 32
#             return self.n
#         raise StopIteration()
#
# for i in getLoadMoreKey(2000):
#     print(i)


# def warpper(func):
#     def deco(*args, **kwargs):
#         categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN', '娱乐': 'ENTERTAINMENT',
#                       '音乐': 'MUSIC', '动漫': 'ANIMATION','文化': 'CULTURE', '科技': 'TECH',
#                       '资讯': 'NEWS', '体育': 'SPORT', '游戏': 'GAME', '财经': 'FINANCE', '生活': 'LIFE'}
#
#         for k, v in categories.items():
#             for i in range(3):
#                 func(v)
#         return func
#
#     return deco
#
# @warpper
# def my_print(post_data):
#     print(post_data)
#
# my_print()


# request_headers = {
#         'Host': 'app.jike.ruguoapp.com',
#         'Accept': '*/*',
#         'App-BuildNo': '1096',
#         'App-Version': '4.3.1',
#         'BundleID': 'com.ruguoapp.jike',
#         'OS': 'ios',
#         'Accept-Language': 'zh-cn',
#         'Accept-Encoding': 'br,gzip,deflate',
#         'Content-Type': 'application/json',
#         'Manufacturer': 'Apple',
#         'User-Agent': '%E5%8D%B3%E5%88%BB/1096 CFNetwork/897.15 Darwin/17.5.0',
#         'Connection': 'keep-alive'
#     }
# print(request_headers)
# print(type(request_headers))

# class getLoadMoreKey(object):
#     """loadMoreKey: post参数"""
#
#     def __init__(self, max_limit):
#         self.max_limt = max_limit
#         self.n = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max_limt:
#             self.n += 32
#             return self.n
#         raise StopIteration()
# a = getLoadMoreKey(200)
# for i in a:
#     print(i)
# data_arr = []
# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
#     table = book.sheet_by_name('name')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         # print(type(trdata))
#         if 'http://www.miaopai.com/' in trdata[0]:
#             data_arr.append(trdata[0])
# print(data_arr)
# print(len(data_arr))
# import base64
# a = '刺激战场'
# b = base64.b64encode(a.encode('utf-8'))
# #print((base64.b64decode(b)).decode('utf-8'))
# print(b)
# print(b.decode())
# a = '刺激战场'
# b = base64.b64encode(a.encode('utf-8'))
# #print((base64.b64decode(b)).decode('utf-8'))
# print(b)
# print(b.decode())
# a = '23'
# print(int(a))

# from selenium import webdriver
# browser = webdriver.Chrome(executable_path='F:/chromedriver.exe')
# browser.get('http://www.renrenlab.com')
# import time
# time.sleep(10)
# browser.quit()
# import re
# a = 'http://www.meipai.com/media/989143153?uid=1576223931&client_id=1089857302'
#
# b = re.findall(r'http://www.meipai.com/media/\d*', a)
# c = re.findall(r'/\d*', a)
# print(b)
# import re
# data_arr = []
#
# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\1.xlsx') as book:
#     table = book.sheet_by_name('qita')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'http://www.meipai.com/' in trdata[0]:
#             a = re.findall(r'http://www.meipai.com/media/\d*', trdata[0])[0]
#             data_arr.append(a)
# print(len(data_arr))
# import re
# from urllib import parse
# a = 'type=feedvideo&objectid=1034:ec316b81d1d459c761106f4bdd540cc7&mid=4049368656490844&fnick=%E4%B8%80%E4%B8%AAApp%E5%B7%A5%E4%BD%9C%E5%AE%A4&uid=1766610575&video_src=%2F%2Fus.sinaimg.cn%2F003cCSn5jx076X4TZk6s05040100BniY0k01.mp4%3Flabel%3Dmp4_hd%26Expires%3D1526474612%26ssig%3DMPIEG6saNM%26KID%3Dunistore%2Cvideo&playerType=proto&cover_img=http%3A%2F%2Fww2.sinaimg.cn%2Forj480%2F736f0c7ejw1fag0puoqfcj20g008g0u9.jpg&card_height=304&card_width=576&keys=4049368658264228&short_url=&play_count=2234&duration=356&encode_mode=crf&bitrate=188'
# b = re.match(r'.*cover_img=(.*)&card_height', a).group(1)
# c = parse.unquote(b)
# d = re.match(r'.*play_count=(.*)&duration', a).group(1)
# if d:
#     print(b)
# print(c)
# print(type(d))
# print(d)
import time
# b = []
# for i in range(859):
#     a = int(round(time.time()*1000))
#     b.append(a)
# print(b)
# print(len(b))

# import random
# d = []
# for i in range(100):
#     a = random.sample([random.randint(1, 100000000)], 1)
#     b = int(round(time.time()*1000))
#     c = a[0] + b
#     print(a)
#     d.append(c)
# print(d)
import time
# import random
# _s = random.sample([random.randint(1, 100000000)], 1)
# print(_s)
# import base64
# a = base64.b64encode(''.encode('utf-8')).decode()
# print(a)

# from selenium import webdriver
# browser = webdriver.Chrome(executable_path="F:/chromedriver.exe")
# browser.get('https://weibo.com/tv/v/80528b2110a536920878daa8588e570d?fid=1034:80528b2110a536920878daa8588e570d')
# import time
# time.sleep(5)
# video = browser.find_element_by_xpath('//div[@class="con-2 hv-pos hv-center"]/video')
# print(video)
# video.click()
# browser.execute_script("$(arguments[0]).click()", video)

# from urllib import request
# from PIL import Image
# from io import StringIO, BytesIO
# from io import BytesIO
# path = "http://image.pearvideo.com/cont/20180502/cont-1335699-11197347.jpg"
# file = request.urlopen(path)
# print(file.read())
# tmpIm = BytesIO(file.read())
# img = Image.open(r'C:\Users\zc-yy\Desktop\cont-1338889-11208528.png')
# print(img.size)
# #
# # #print()        # JPEG
# print(img.size)           # (801, 1200)

# from io import BytesIO
#
# # write to BytesIO:
# f = BytesIO()
# f.write(b'hello')
# f.write(b' ')
# f.write(b'world!')
# print(f.getvalue())
#
# # read from BytesIO:
# data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
# f = BytesIO(data)
# print(f.read())
# from queue import Queue
# q = Queue(maxsize=100)
# for i in range(11):
#     q.put(i)
# if q.not_empty:
#     for i in range(q.qsize()):
#         print(q.get())
# import re
# data_arr = []
#
# with xlrd.open_workbook(r'C:\Users\zc-yy\Desktop\2.xlsx') as book:
#     table = book.sheet_by_name('tiyuyouxi')
#     row_count = table.nrows
#     for row in range(1, row_count):
#         trdata = table.row_values(row)
#         if 'https://www.meipai.com/' in trdata[0]:
#             a = re.findall(r'https://www.meipai.com/media/\d*', trdata[0])[0]
#             data_arr.append(a)
#         # elif 'http://www.meipai.com/' in trdata[0]:
#         #     a = re.findall(r'http://www.meipai.com/media/\d*', trdata[0])[0]
#         #     data_arr.append(a)
# print(data_arr)
# print(len(data_arr))
# import re
#
# a = 'https://m.365yg.com/group/6555805421561446915'
# b = re.match(r'.*group/(\d+)', a).group(1)
# print(b)
# from hashlib import md5
# from string import ascii_letters, digits
# from itertools import permutations
# from time import time
#
# all_letters = ascii_letters + digits + '.,;'
#
#
# def decrypt_md5(md5_value):
#     if len(md5_value) != 32:
#         print('error')
#         return
#     md5_value = md5_value.lower()
#     for k in range(5, 10):
#         for item in permutations(all_letters, k):
#             item = ''.join(item)
#             print('.', end='')
#             if md5(item.encode()).hexdigest() == md5_value:
#                 return item
#
#
# md5_value = 'e7d057704ea5206d8cb61280741238f5'
# start = time()
# result = decrypt_md5(md5_value)
# if result:
#     print('\n Success: ' + md5_value + '==>' + result)
# print('Time used:', time() - start)
# a = 'https://app.bilibili.com/v2/playurl?' \
#     'appkey=YvirImLGlLANCLvM' \
#     '&build=6680' \
#     '&buvid=1134402fc290d710313b9db99e310eed&' \
#     'cid=39922399' \
#     '&device=phone' \
#     '&otype=json' \
#     '&platform=iphone' \
#     '&qn=16' \
#     '&sign=36e8ec6971b6c089409aea3ee9ecbf64'

# a = {'build': '6680', 'buvid': '1134402fc290d710313b9db99e310eed',
#      'cid': '39922399', 'device': 'phone', 'otype': 'json', 'platform': 'iphone',
#      'qn': '16', 'appkey': 'YvirImLGlLANCLvM'}
# from urllib import parse
# import hashlib
#
#
# def GetSign(params, appkey, AppSecret=None):
#     params['appkey'] = appkey
#     data = ""
#     paras = params.keys()
#     #print(list(params.keys()))
#     sorted(paras)
#     data = parse.urlencode(params)
#     #print(data)
#     if AppSecret == None:
#         return data
#     m = hashlib.md5()
#     m.update(data + AppSecret)
#     return data + '&sign=' + m.hexdigest()
#
#
# if __name__ == '__main__':
#     print(GetSign(a, 'YvirImLGlLANCLvM', AppSecret=None))
# keys = a.keys()
# print(keys)
# b = [1,2,3]
# print(sorted(b, reverse=True))
# s_keys = sorted(keys, reverse=True)
# print(list(s_keys))

# new_dic = a[s_keys[0]]+a[s_keys[1]]+a[s_keys[2]]+a[s_keys[3]]+a[s_keys[4]]+a[s_keys[5]]+a[s_keys[6]]
# print(new_dic)
# data = ''
# for i in list(s_keys):
#     data = data+i+a[i]
# print(data)
import random

# __RANDOM_TOKENS = "0123456789ABCDEF"
#
#
# def random_str(length, radix=16) -> str:
#     import random
#     s = []
#
#     for i in range(0, length):
#         s.append(__RANDOM_TOKENS[random.randrange(1, min(16, radix))])
#
#     return "".join(s)
#
# if __name__ == '__main__':
#     cuid = random_str(32, radix=16).upper() + '|' + random_str(15, radix=10)
#     print(cuid)


# a = {'name': 'zhangcong'}
# b = a.update({'age': 18})
# print(b)
from scrapy.http import Request
import time