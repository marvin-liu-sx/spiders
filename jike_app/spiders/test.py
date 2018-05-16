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
import re
from urllib import parse
a = 'type=feedvideo&objectid=1034:ec316b81d1d459c761106f4bdd540cc7&mid=4049368656490844&fnick=%E4%B8%80%E4%B8%AAApp%E5%B7%A5%E4%BD%9C%E5%AE%A4&uid=1766610575&video_src=%2F%2Fus.sinaimg.cn%2F003cCSn5jx076X4TZk6s05040100BniY0k01.mp4%3Flabel%3Dmp4_hd%26Expires%3D1526474612%26ssig%3DMPIEG6saNM%26KID%3Dunistore%2Cvideo&playerType=proto&cover_img=http%3A%2F%2Fww2.sinaimg.cn%2Forj480%2F736f0c7ejw1fag0puoqfcj20g008g0u9.jpg&card_height=304&card_width=576&keys=4049368658264228&short_url=&play_count=2234&duration=356&encode_mode=crf&bitrate=188'
b = re.match(r'.*cover_img=(.*)&card_height', a).group(1)
c = parse.unquote(b)
d = re.match(r'.*play_count=(.*)&duration', a).group(1)
if d:
    print(d)
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
#browser.execute_script("$(arguments[0]).click()", video)















