# -*- coding: utf-8 -*-

from scrapy import signals


class JikeAppSpiderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):

        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):

        return None

    def process_spider_output(self, response, result, spider):

        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):

        pass

    def process_start_requests(self, start_requests, spider):

        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JikeAppDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


from selenium import webdriver
from scrapy.http import HtmlResponse


class JSPageMiddleware(object):

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="F:/chromedriver.exe")
        super(JSPageMiddleware, self).__init__()

    def process_request(self, request, spider):
        if spider.name == 'meipai':
            self.browser.get(request.url)
            import time
            time.sleep(5)
            print('middleware启动')
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,
                                encoding='utf-8', request=request)
