# _*_coding:utf-8_*_
# Time : 2018/6/7 11:09
# User : yy-zhangcong2
# Email: zhangcong2@yy.com
# Python: 3.6.4

"""Documentation comments"""
from tools.db_config import db_config as df

import pymysql
import logging

_l = logging.getLogger(__file__)

class MysqlDB:
    def __init__(self):
        try:
            self.connect = pymysql.Connect(
                host=df['host'],
                port=df['port'],
                user=df['user'],
                password=df['password'],
                db=df['database'],
                charset=df['charset']
            )
            #_l.info('db-connect-success')
            print('db-connect-success')
        except Exception as e:
            print(e)
            #_l.info('dn-connect-failed')
            print('dn-connect-failed')
        self.cursor = self.connect.cursor()

    def close(self):
        if self.connect and self.cursor:
            self.cursor.close()
            self.connect.close()
            #_l.info('db-close-success')
            print('db-close-success')
        else:
            #_l.info('db-close-failed')
            print('db-close-failed')

    def insert(self, sql, data):
        if isinstance(sql, str):
            try:
                self.cursor.execute(sql % data)
                self.connect.commit()
            except Exception as e:
                self.connect.rollback()
                raise e
