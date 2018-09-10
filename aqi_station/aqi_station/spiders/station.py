# -*- coding: utf-8 -*-
import scrapy
from aqi_station.items import StationItem

class StationSpider(scrapy.Spider):
    name = 'station'
    #allowed_domains = ['www.aqistudy.cn']
    start_urls = ['http://www.nmc.cn/publish/forecast/ABJ/chaoyang.html']

    def parse(self, response):
        districts = response.xpath('//select[@id="citySel"]/option')[1:]
        for district in districts:
            url = "http://www.nmc.cn" + district.xpath('./@url').extract_first()
            yield (scrapy.Request(url, callback = self.parse_detail))

    def parse_detail(self, response):
        item = StationItem()
        item["city_name"] = response.xpath('//div[@class="cname fl"]/text()').extract_first().strip()
        item["date"] = response.xpath('//span[@id="realPublishTime"]/text()').extract_first()
        item["temp"] = response.xpath('//span[@id="realTemperature"]/text()').extract_first()
        item["rain"] = response.xpath('//span[@id="realRain"]/text()').extract_first()
        item["wind_direction"] = response.xpath('//span[@id="realWindDirect"]/text()').extract_first()
        item["wind_power"] = response.xpath('//span[@id="realWindPower"]/text()').extract_first()
        item["humidity"] = response.xpath('//span[@id="realHumidity"]/text()').extract_first()
        yield item
