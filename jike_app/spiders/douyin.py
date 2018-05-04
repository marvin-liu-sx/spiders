# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import time
import json
from ..items import DouyinItem
import logging

_l = logging.getLogger(__name__)


class DouyinSpider(scrapy.Spider):
    name = 'douyin'
    allowed_domains = ['aweme.snssdk.com']
    # start_urls = ['http://www.baidu.com/']

    current_time = int(time.time())
    default_headers = {
        'Host': 'aweme.snssdk.com',
        'Accept': '*/*',
        'User-Agent': 'Aweme/1.7.9 (iPhone; iOS 11.3; Scale/2.00)',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'Accept-Encoding': 'br,gzip,deflate',
        'Connection': 'keep-alive',
        # 'Cookie': 'install_id=31717878106; odin_tt=61493451513970616d4d765441634375947e5e5648add0aa69c062e39cd72cd95aa376bdd5e8c1741579a6043d0086df; ttreq=1$5fe4fb1448254ccdfb47c989eced6965690bcf31'
    }

    def start_requests(self):
        for i in range(100000):
            yield Request(url='https://aweme.snssdk.com/aweme/v1/feed/?iid=31717878106&ac=WIFI&os_api=18&app_name=aweme&channel=App%20Store&idfa=80DEEA4B-2DC9-43FE-A097-4619DFBF8468&device_platform=iphone&build_number=17909&vid=787FF51A-8429-4C9D-93C1-27A6CD0AE7D8&openudid=93d55ca4a7fd3596e0ee7434610d3c1aac90c8f7&device_type=iPhone7,1&app_version=1.7.9&device_id=10258085598&version_code=1.7.9&os_version=9.3.2&screen_width=1125&aid=1128&count=6&feed_style=0&max_cursor=0&pull_type=2&type=0&volume=0.00&mas=005b02de53fb5fdf37ee286c63517a73537c917776712366ee80c7&as=a175f25ee56fdab46c1872&ts=1525425397', method='GET',
                          headers=self.default_headers,
                          callback=self.parse,
                          dont_filter=True)

    def parse(self, response):
        meta_data = json.loads(response.body, encoding='utf-8')
        if 'aweme_list' in meta_data.keys() and meta_data['aweme_list']:
            _l.info('aweme_list is not None, logid is %s' % meta_data['extra']['logid'])
            dy_item = DouyinItem()
            for obj_dict in meta_data['aweme_list']:
                if obj_dict['is_ads'] is True:
                    pass
                else:
                    if 'aweme_id' in obj_dict.keys() and obj_dict['aweme_id']:
                        dy_item['video_id'] = obj_dict['aweme_id']
                    else:
                        dy_item['video_id'] = 'unknow'

                    if 'video' in obj_dict.keys() and 'origin_cover' in obj_dict['video'].keys() and obj_dict['video']['origin_cover']['url_list'][0]:
                        dy_item['video_img'] = obj_dict['video']['origin_cover']['url_list'][0]
                    else:
                        dy_item['video_img'] = 'unknow'

                    if 'video'in obj_dict.keys() and 'download_addr'in obj_dict['video'].keys() and obj_dict['video']['download_addr']['url_list'][0]:
                        dy_item['video_url'] = obj_dict['video']['download_addr']['url_list'][0]
                    else:
                        dy_item['video_url'] = 'unknow'

                    if 'desc'in obj_dict.keys() and obj_dict['desc']:
                        dy_item['video_title'] = obj_dict['desc']
                    else:
                        dy_item['video_title'] = 'unknow'

                    if 'video'in obj_dict.keys() and 'width'in obj_dict['video'].keys() and obj_dict['video']['width']:
                        dy_item['video_width'] = obj_dict['video']['width']
                    else:
                        dy_item['video_width'] = 'unknow'

                    if 'video'in obj_dict.keys() and 'height'in obj_dict['video'].keys() and obj_dict['video']['height']:
                        dy_item['video_height'] = obj_dict['video']['height']
                    else:
                        dy_item['video_height'] = 'unknow'

                    if 'video'in obj_dict.keys() and 'duration'in obj_dict['video'].keys() and obj_dict['video']['duration']:
                        dy_item['video_duration'] = obj_dict['video']['duration']
                    else:
                        dy_item['video_duration'] = 'unknow'

                    if 'statistics'in obj_dict.keys() and 'play_count'in obj_dict['statistics'].keys() and obj_dict['statistics']['play_count']:
                        dy_item['play_count'] = obj_dict['statistics']['play_count']
                    else:
                        dy_item['play_count'] = 'unknow'

                    if 'statistics'in obj_dict.keys() and 'comment_count'in obj_dict['statistics'].keys() and obj_dict['statistics']['comment_count']:
                        dy_item['comment_count'] = obj_dict['statistics']['comment_count']
                    else:
                        dy_item['comment_count'] = 'unknow'

                    if 'statistics'in obj_dict.keys() and 'share_count'in obj_dict['statistics'].keys() and obj_dict['statistics']['share_count']:
                        dy_item['share_count'] = obj_dict['statistics']['share_count']
                    else:
                        dy_item['share_count'] = 'unknow'

                    if 'statistics'in obj_dict.keys() and 'digg_count'in obj_dict['statistics'].keys() and obj_dict['statistics']['digg_count']:
                        dy_item['digg_count'] = obj_dict['statistics']['digg_count']
                    else:
                        dy_item['digg_count'] = 'unknow'

                    dy_item['video_source'] = '1'
                    yield dy_item
        else:
            _l.info('aweme_list is None, logid id  is %s' % meta_data['extra']['logid'])


















