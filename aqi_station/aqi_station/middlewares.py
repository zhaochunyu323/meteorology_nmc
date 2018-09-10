# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import logging
import time
from scrapy.http import HtmlResponse
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import FirefoxOptions

class StationDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        # 有界面
        firefox_options = FirefoxOptions()
        firefox_options.set_headless()
        self.driver = webdriver.Firefox(options = firefox_options)
        # 无界面
        # self.options = Options()
        # self.options.set_headless()
        # self.driver = webdriver.Chrome(options = self.options)

    def process_request(self,spider,request):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            html = self.driver.page_source
            return HtmlResponse(url=self.driver.current_url,
                                    body=html,
                                    encoding='utf-8',
                                    request=request)
        except:
            logging.error("该地址没有信息：%s" % request.url)

    def __del__(self):
        self.driver.close()
