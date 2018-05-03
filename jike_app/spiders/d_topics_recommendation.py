# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from ..items import DRecommenDationItem
from tools.fake_request_headers import RandomHeaders


class getLoadMoreKey(object):
    """loadMoreKey: post参数"""

    def __init__(self, max_limit):
        self.max_limt = max_limit
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max_limt:
            self.n += 32
            return self.n
        raise StopIteration()


def warpper(func):
    def deco(*args, **kwargs):
        # categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN', '娱乐': 'ENTERTAINMENT',
        #               '音乐': 'MUSIC', '动漫': 'ANIMATION','文化': 'CULTURE', '科技': 'TECH',
        #               '资讯': 'NEWS', '体育': 'SPORT', '游戏': 'GAME', '财经': 'FINANCE', '生活': 'LIFE'}
        categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN'}

        release = False
        max_limit = 200
        if release:
            for k, v in categories.items():
                post_data = {"categoryAlias": v}
                func(post_data)
        else:
            for k, v in categories.items():
                for i in getLoadMoreKey(max_limit):
                    post_data = {"loadMoreKey": i, "categoryAlias": v}
                    func(post_data)
        return func

    return deco


class DTopicsRecommendationSpider(scrapy.Spider):
    name = 'd_topics_recommendation'
    allowed_domains = ['app.jike.ruguoapp.com']

    # start_urls = ['http://app.jike.ruguoapp.com/']

    # request_headers = {
    #     'Host': 'app.jike.ruguoapp.com',
    #     'Accept': '*/*',
    #     'App-BuildNo': '1096',
    #     'App-Version': '4.3.1',
    #     'BundleID': 'com.ruguoapp.jike',
    #     'OS': 'ios',
    #     'Accept-Language': 'zh-cn',
    #     'Accept-Encoding': 'br,gzip,deflate',
    #     'Content-Type': 'application/json',
    #     'Manufacturer': 'Apple',
    #     'User-Agent': '%E5%8D%B3%E5%88%BB/1096 CFNetwork/897.15 Darwin/17.5.0',
    #     'Connection': 'keep-alive'
    # }

    # @warpper
    # def start_requests(self, **kwargs):
    #     yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list', headers=self.request_headers,
    #                   method='POST', body=str(kwargs).replace('\'', '"'), callback=self.parse)

    def start_requests(self):
        categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN', '娱乐': 'ENTERTAINMENT',
                      '音乐': 'MUSIC', '动漫': 'ANIMATION', '文化': 'CULTURE', '科技': 'TECH',
                      '资讯': 'NEWS', '体育': 'SPORT', '游戏': 'GAME', '财经': 'FINANCE', '生活': 'LIFE'}
        release = True
        max_limit = 2000
        if release:
            for k, v in categories.items():
                post_data = {"categoryAlias": v}
                yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list',
                              headers=randomHeaders().get_header(), method='POST', meta={'category': k},
                              body=str(post_data).replace('\'', '"'), callback=self.parse)
        else:
            for k, v in categories.items():
                for i in getLoadMoreKey(max_limit):
                    post_data = {"loadMoreKey": i, "categoryAlias": v}
                    yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list',
                                  headers=randomHeaders().get_header(), method='POST', meta={'category': k},
                                  body=str(post_data).replace('\'', '"'), callback=self.parse)

    def parse(self, response):
        dic_result = json.loads(str(response.body, encoding='utf-8'))

        item = DRecommenDationItem()
        category = response.meta['category']
        for obj_dic in dic_result['data']:
            item['id'] = obj_dic['id']
            item['category'] = category
            item['content'] = obj_dic['content']
            item['topicId'] = obj_dic['topicId']
            item['subscribersCount'] = obj_dic['subscribersCount']
            item['thumbnailUrl'] = obj_dic['thumbnailUrl']
            yield item
