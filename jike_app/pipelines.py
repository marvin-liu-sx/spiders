# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter
import json
import codecs
import pymysql
import pymysql.cursors
from twisted.enterprise import adbapi


class JikeAppPipeline(object):
    def process_item(self, item, spider):
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            password='qwer@6a',
            db='jike_app',
            charset='utf8'
        )
        cursor = connect.cursor()
        sql = "INSERT INTO jike_recommendation (category, re_id, re_topic_id, re_content, re_subscribersCount, re_thumbnailUrl)" \
              " VALUES ('%s','%s','%s','%s','%s', '%s')"
        data = (
            item['category'], item['id'], item['topicId'], item['content'], item['subscribersCount'],
            item['thumbnailUrl'])
        try:
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()
            raise e
        finally:
            connect.commit()
            cursor.close()
            connect.close()
        return item


class JikeMessagesPipeline(object):
    def process_item(self, item, spider):
        connect = pymysql.Connect(
            host='221.228.79.244',
            port=8066,
            user='zhangcong2@SpiderTest',
            password='4k7wtlqqR',
            db='spider_test',
            charset='utf8mb4'
        )
        cursor = connect.cursor()
        sql = "INSERT INTO jike_messages_new (topic_category, topic_content, topic_type, topic_focus_count, " \
              "message_id, message_type, message_content, message_status, message_like_count, message_comment_count, " \
              "message_repost_count, message_is_video, message_is_img)" \
              " VALUES ('%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        data = (
            item['topic_category'], item['topic_content'], item['topic_type'], item['topic_focus_count'], item['id'],
            item['type'], item['content'], item['status'], item['like_count'], item['comment_count'],
            item['repost_count'], item['is_video'], item['is_img'])
        try:
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()
            raise e
        finally:
            connect.commit()
            cursor.close()
            connect.close()
        return item


# **********************************************************************************************************************
# 1
class JsonWithEncodingPipline(object):
    def __init__(self):
        self.file = codecs.open('topics.json', 'wb', encoding='utf-8')

    def process_itme(self, item, spider):
        lines = json.dumps(item, ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def close_spider(self, spider):
        self.file.close()


# **********************************************************************************************************************
# 2
class JsonExporterPipleline(object):
    def __init__(self):
        self.file = open('topics2.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


# **********************************************************************************************************************

class MysqlTwistedPipline(object):
    """异步insert"""

    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf-8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True
        )

        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql, params)


class DouYinPipline(object):
    """
    抖音item
    """

    def process_item(self, item, spider):
        connect = pymysql.Connect(
            host='221.228.79.244',
            port=8066,
            user='zhangcong2@SpiderTest',
            password='4k7wtlqqR',
            db='spider_test',
            charset='utf8mb4'
        )
        cursor = connect.cursor()
        sql = "INSERT INTO douyin (video_source, video_id, video_img, video_url, video_title, video_width, video_height," \
              " video_duration, play_count, comment_count, share_count, digg_count)" \
              " VALUES ('%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        data = (
            item['video_source'], item['video_id'], item['video_img'], item['video_url'], item['video_title'],
            item['video_width'], item['video_height'], item['video_duration'], item['play_count'], item['comment_count'],
            item['share_count'], item['digg_count'])
        try:
            cursor.execute(sql % data)
        except Exception as e:
            connect.rollback()
            raise e
        finally:
            connect.commit()
            cursor.close()
            connect.close()
        return item
########################################################################################################################
class MiaoPaiPipline(object):
    def process_item(self, item, spider):
        connect = pymysql.Connect(
            host='221.228.79.244',
            port=8066,
            user='zhangcong2@SpiderTest',
            password='4k7wtlqqR',
            db='spider_test',
            charset='utf8mb4'
        )
        cursor = connect.cursor()
        sql = "INSERT INTO yunying (i_id, channel_id, media_id, media_name, video_id, video_title, play_count, video_duration," \
              " video_url, video_cover, source, status, meta_data, video_width, video_height)" \
              " VALUES ('%s','%s','%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        data = (
            item['i_id'], item['channel_id'], item['media_id'], item['media_name'], item['video_id'], item['video_title'],
            item['play_count'], item['video_duration'], item['video_url'], item['video_cover'], item['source'],
            item['status'], item['meta_data'], item['video_width'], item['video_height'])
        try:
            cursor.execute(sql % data)
            connect.commit()
        except Exception as e:
            connect.rollback()
            raise e
        finally:
            cursor.close()
            connect.close()
        return item