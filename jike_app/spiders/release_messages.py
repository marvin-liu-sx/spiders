# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from tools.fake_request_headers import RandomHeaders
from ..items import DMessagesItem


class ReleaseMessagesSpider(scrapy.Spider):
    name = 'release_messages'
    allowed_domains = ['app.jike.ruguoapp.com']

    # start_urls = ['http://app.jike.ruguoapp.com/']

    post_headers = {
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
        'Connection': 'keep-alive'
    }

    # categories = {'推荐': 'RECOMMENDATION'}

    categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN', '娱乐': 'ENTERTAINMENT',
                  '音乐': 'MUSIC', '动漫': 'ANIMATION', '文化': 'CULTURE', '科技': 'TECH',
                  '资讯': 'NEWS', '体育': 'SPORT', '游戏': 'GAME', '财经': 'FINANCE', '生活': 'LIFE'}
    def start_requests(self):
        post_data = {"areaCode": "+86", "password": "yangcongtouGG@6a", "mobilePhoneNumber": "15210583831"}
        return [Request(url='https://app.jike.ruguoapp.com/1.0/users/loginWithPhoneAndPassword',
                        headers=self.post_headers, meta={'cookiejar': 1}, method='POST',
                        body=str(post_data).replace('\'', '\"'), callback=self.after_login)]

    def after_login(self, response):
        dict_result = json.loads(response.body.decode(), encoding='utf-8')
        user_id = dict_result['user']['id']
        if user_id is not None:
            print('登录成功id为：>>>>>>>>>' + user_id)
            for k, v in self.categories.items():
                post_data = {"categoryAlias": v}
                meta_dict = {'category': k, 'cookiejar': response.meta['cookiejar']}
                yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list',
                              headers=self.post_headers, method='POST', meta=meta_dict,
                              body=str(post_data).replace('\'', '"'), callback=self.parse)
        else:
            print('登录失败')

    # 获取id
    def parse(self, response):
        dic_result = json.loads(str(response.body, encoding='utf-8'))
        print(len(dic_result['data']))
        for obj_dic in dic_result['data']:
            re_id = obj_dic['id']
            post_data = {"topic": re_id, "limit": 20}
            meta_dict = {'category': response.meta['category'], 'content': obj_dic['content'],
                         'cookiejar': response.meta['cookiejar'], 'topictype': obj_dic['topicType'],
                         'subscribersCount': obj_dic['subscribersCount']}
            yield Request(url='https://app.jike.ruguoapp.com/1.0/messages/history',
                          headers=self.post_headers,
                          method='POST', meta=meta_dict, body=str(post_data).replace('\'', '"'),
                          callback=self.detail_parse)

    # messages 内容
    def detail_parse(self, response):
        dic_result = json.loads(str(response.body, encoding='utf-8'))
        item = DMessagesItem()
        print(response.meta['category'])
        print(response.meta['content'])
        print(len(dic_result['data']))
        for obj_dict in dic_result['data']:
            if 'id' in obj_dict.keys() and obj_dict['id']:
                item['id'] = obj_dict['id']
            else:
                item['id'] = 'unkown'

            if 'type' in obj_dict.keys() and obj_dict['type']:
                item['type'] = obj_dict['type']
            else:
                item['type'] = 'unkown'

            if 'content' in obj_dict.keys() and obj_dict['content']:
                item['content'] = obj_dict['content']
            else:
                item['content'] = 'nukown'

            if 'status' in obj_dict.keys() and obj_dict['status']:
                item['status'] = obj_dict['status']
            else:
                item['status'] = 'unkown'

            if 'likeCount' in obj_dict.keys() and obj_dict['likeCount']:
                item['like_count'] = obj_dict['likeCount']
            else:
                item['like_count'] = '0'

            if 'commentCount' in obj_dict.keys() and obj_dict['commentCount']:
                item['comment_count'] = obj_dict['commentCount']
            else:
                item['comment_count'] = '0'

            if 'repostCount' in obj_dict.keys() and obj_dict['repostCount']:
                item['repost_count'] = obj_dict['repostCount']
            else:
                item['repost_count'] = '0'

            # if 'createdAt' in obj_dict.keys() and obj_dict['createdAt']:
            #     item['create_time'] = obj_dict['createdAt']
            # else:
            #     item['create_time'] = 'no_data'

            if 'pictures' in obj_dict.keys() and obj_dict['pictures']:
                item['is_img'] = '1'
            else:
                item['is_img'] = '0'

            if 'video' in obj_dict.keys() and obj_dict['video']:
                item['is_video'] = '1'
            else:
                item['is_video'] = '0'

            item['topic_category'] = response.meta['category']
            item['topic_content'] = response.meta['content']
            item['topic_type'] = response.meta['topictype']
            item['topic_focus_count'] = response.meta['subscribersCount']
            yield item
