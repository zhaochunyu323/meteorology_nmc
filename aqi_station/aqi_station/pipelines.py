# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class StationPipeline(object):
    def open_spider(self,spider):
        # 打开csv文件对象
        self.csv_file = open('weather.csv','a')
        # 把csv对象定位写入对象
        self.csv_writer=csv.writer(self.csv_file)
        # 定义表头
        #table_title = ["city_name", "date", "temp", "rain", "wind_direction", "wind_power", "humidity"]
        # 写入表头
        # 一次写入多行使用writerows
        #self.csv_writer.writerow(table_title)

    def process_item(self, item, spider):
#        item["source"] = spider.name
        item = dict(item)
        # 根据表头按顺序写入数据
        self.csv_writer.writerow((item["city_name"],item["date"],item["temp"],item["rain"],item["wind_direction"],item["wind_power"],item["humidity"]))

        return item

    def close_spider(self,spider):
        self.csv_file.close()
