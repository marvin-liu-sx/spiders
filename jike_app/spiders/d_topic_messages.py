# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
from tools.fake_request_headers import RandomHeaders
from ..items import DMessagesItem, jikeAppItemLoader


class DTopicMessagesSpider(scrapy.Spider):
    name = 'd_topic_messages'
    allowed_domains = ['app.jike.ruguoapp.com']

    # start_urls = ['http://app.jieke.ruoguoapp.com/']

    # categories = {'体育': 'SPORT'}
    categories = {'推荐': 'RECOMMENDATION', '趣味': 'FUN', '娱乐': 'ENTERTAINMENT',
                  '音乐': 'MUSIC', '动漫': 'ANIMATION', '文化': 'CULTURE', '科技': 'TECH',
                  '资讯': 'NEWS', '体育': 'SPORT', '游戏': 'GAME', '财经': 'FINANCE', '生活': 'LIFE'}

    def start_requests(self):
        for k, v in self.categories.items():
            post_data = {"categoryAlias": v}
            meta_dict = {'category': k, 'cookiejar': 1, 'cate_value': v}
            yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list',
                          headers=RandomHeaders().get_header(), method='POST', meta=meta_dict,
                          body=str(post_data).replace('\'', '"'), callback=self.parse)

    # 列表页
    def parse(self, response):
        dic_result = json.loads(str(response.body, encoding='utf-8'))
        print(response.meta['category'] + '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print(type(dic_result['loadMoreKey']))
        num = dic_result['loadMoreKey']
        if dic_result['loadMoreKey'] is not None and dic_result['loadMoreKey'] < 30:
            for obj_dict in dic_result['data']:
                print(obj_dict['content'])
                post_data = {'limit': 20, 'topic': obj_dict['id']}
                meta_dict = {'category': response.meta['category'], 'content': obj_dict['content'],
                             'cookiejar': response.meta['cookiejar'], 'topictype': obj_dict['topicType'],
                             'subscribersCount': obj_dict['subscribersCount'], 'topic': obj_dict['id']}
                yield Request(url='https://app.jike.ruguoapp.com/1.0/messages/history',
                              headers=RandomHeaders().get_header(), method='POST', meta=meta_dict,
                              body=str(post_data).replace('\'', '"'), callback=self.detail_parse)
            v = response.meta['cate_value']
            meta_dict = {'category': response.meta['category'], 'cookiejar': response.meta['cookiejar'],
                         'cate_value': v}
            post_data = {'loadMoreKey': num, 'categoryAlias': v}
            yield Request(url='https://app.jike.ruguoapp.com/1.0/topics/recommendation/list',
                          headers=RandomHeaders().get_header(), method='POST', meta=meta_dict,
                          body=str(post_data).replace('\'', '"'), callback=self.parse)

    # 内容页
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

        if dic_result['loadMoreKey'] is not None:
            post_data = {'limit': 10, 'topic': response.meta['topic'], 'loadMoreKey': dic_result['loadMoreKey']}
            meta_dict = {'category': response.meta['category'], 'content': response.meta['content'],
                         'cookiejar': response.meta['cookiejar'], 'topictype': response.meta['topictype'],
                         'subscribersCount': response.meta['subscribersCount'], 'topic': response.meta['topic']}
            yield Request(url='https://app.jike.ruguoapp.com/1.0/messages/history',
                          headers=RandomHeaders().get_header(), method='POST', meta=meta_dict,
                          body=str(post_data).replace('\'', '"'), callback=self.detail_parse)
