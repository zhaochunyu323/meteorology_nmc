# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city_name = scrapy.Field()
    date = scrapy.Field()
    temp = scrapy.Field()
    wind_direction = scrapy.Field()
    wind_power = scrapy.Field()
    humidity = scrapy.Field()
    rain = scrapy.Field()
