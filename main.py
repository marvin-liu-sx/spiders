# _*_coding:utf-8_*_
# Time : 2018/4/18 16:03
# User : zc-yy
# Email: zhangcong2@yy.com


"""Documentation comments"""

import sys, os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'miaopai'])
