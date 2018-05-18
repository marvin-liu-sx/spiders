# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


# def set_default_value(value):
#     if value is None or '':
#         return 'no_data'


class jikeAppItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DRecommenDationItem(scrapy.Item):
    """
    主题字段
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    category = scrapy.Field()
    content = scrapy.Field()
    topicId = scrapy.Field()
    subscribersCount = scrapy.Field()
    thumbnailUrl = scrapy.Field()

    def get_insert_sql(self):
        insert_sql = "insert into jike_recommendation(category, re_id, re_topic_id, re_content, re_subscribersCount, re_thumbnailUrl)" \
                     " VALUES (%s, %s, %s, %s, %s, %s)"
        params = (
            self["category"], self["id"], self["topicId"], self["content"], self["subscribersCount"],
            self["thumbnailUrl"])
        return insert_sql, params


class DMessagesItem(scrapy.Item):
    """
    主题内容字段
    """
    topic_category = scrapy.Field()
    topic_content = scrapy.Field()
    topic_type = scrapy.Field()
    topic_focus_count = scrapy.Field()
    # id
    id = scrapy.Field(

    )
    # 类型
    type = scrapy.Field()
    # 文字信息
    content = scrapy.Field()
    # 状态
    status = scrapy.Field()
    # 点赞数
    like_count = scrapy.Field()
    # 评论数
    comment_count = scrapy.Field()
    # 转发数
    repost_count = scrapy.Field()
    # 时间
    # create_time = scrapy.Field()
    # 是否为视频
    is_video = scrapy.Field()
    # 是否为图文
    is_img = scrapy.Field()


class DouyinItem(scrapy.Item):
    video_source = scrapy.Field()
    video_id = scrapy.Field()
    video_img = scrapy.Field()
    video_url = scrapy.Field()
    video_title = scrapy.Field()
    video_width = scrapy.Field()
    video_height = scrapy.Field()
    video_duration = scrapy.Field()
    play_count = scrapy.Field()
    comment_count = scrapy.Field()
    share_count = scrapy.Field()
    digg_count = scrapy.Field()

class MiaoPaiItem(scrapy.Item):
    i_id = scrapy.Field()
    channel_id = scrapy.Field()
    media_id = scrapy.Field()
    media_name = scrapy.Field()
    video_id = scrapy.Field()
    video_title = scrapy.Field()
    play_count = scrapy.Field()
    video_duration = scrapy.Field()
    video_url = scrapy.Field()
    play_url = scrapy.Field()
    video_cover = scrapy.Field()
    source = scrapy.Field()
    status = scrapy.Field()
    meta_data = scrapy.Field()
    video_width = scrapy.Field()
    video_height = scrapy.Field()
