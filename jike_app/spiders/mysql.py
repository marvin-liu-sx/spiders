# _*_coding:utf-8_*_
# Time : 2018/5/8 10:06
# User : yy-zhangcong2
# Email: zhangcong2@yy.com
# Python: 3.6.4

"""Documentation comments"""

import time
import random
import pymysql
import logging

_l = logging.getLogger(__name__)


class DataProducer(object):
    def __init__(self):
        pass

    @staticmethod
    def process_item():
        connect = pymysql.Connect(
            host='221.228.79.244',
            port=8066,
            user='zhangcong2@SpiderTest',
            password='4k7wtlqqR',
            db='spider_test',
            charset='utf8mb4'
        )
        cursor = connect.cursor()
        sql = "INSERT INTO mydata (i_id) VALUES ('%s')"
        for i in range(63565):
            time.sleep(0.1)
            a = random.sample([random.randint(1, 10000000000)], 1)
            b = int(round(time.time() * 1000))
            data = a[0] + b
            print(data)
            try:
                cursor.execute(sql % data)
                connect.commit()
            except Exception as e:
                connect.rollback()
                raise e
        cursor.close()
        connect.close()


if __name__ == '__main__':
    DataProducer().process_item()
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.submit(DataProducer().process_item())