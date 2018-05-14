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
# a = '28.5万播放'
# b = re.findall(r'\d*', a)
# c = b[0]+b[2]
# print(type(c))