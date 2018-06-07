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
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36"')
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        self.options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(executable_path="F:/chromedriver.exe", chrome_options=self.options)
        super(JSPageMiddleware, self).__init__()

    def process_request(self, request, spider):
        if spider.name == 'sunshine':
            self.browser.get(request.url)
            import time
            time.sleep(8)
            print('middleware启动')
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,
                                encoding='utf-8', request=request)


class WeiboPageMiddleware(object):

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36"')
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2
            }
        }
        self.options.add_experimental_option("prefs", prefs)
        self.browser = webdriver.Chrome(executable_path="F:/chromedriver.exe", chrome_options=self.options)
        super(WeiboPageMiddleware, self).__init__()

    def process_request(self, request, spider):
        if spider.name == 'weibo':
            # options = webdriver.ChromeOptions()
            # options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
            #                      '(KHTML, like Gecko) Chrome/67.0.3371.0 Safari/537.36"')
            # prefs = {
            #     'profile.default_content_setting_values': {
            #         'images': 2
            #     }
            # }
            # options.add_experimental_option("prefs", prefs)
            # browser = webdriver.Chrome(executable_path="F:/chromedriver.exe", chrome_options=options)
            self.browser.get(request.url)
            import time
            time.sleep(5)
            video = self.browser.find_element_by_xpath('.//div[@class="con-2 hv-pos hv-center"]/video')
            print(video)
            video.click()
            print('middleware启动')
            time.sleep(5)
            return HtmlResponse(url=self.browser.current_url, body=self.browser.page_source,
                                encoding='utf-8', request=request)


# 异常的response，记录request信息,调用process_response必须返回response，
# 在process_request里直接返回response，就不再走process_response了
# FormRequest中的FormData最终是加在request.body中的，可以根据request.body拿到
# 可根据request.headers.get()方法拿到request的headers中的key-value值
class CollectFailedRequestHeader(object):
    def process_response(self, request, response, spider):
        if spider.name == '':
            if response.status != 200:
                print('request非200')
                print(request.body.decode())
                with open('formdata.txt', 'a', encoding='utf-8') as b:
                    b.write(request.body.decode()+'\n')
            else:
                pass
                # print(request.headers.get('Cookie').decode())
                # print(request.body.decode())
        else:
            pass
        return response
