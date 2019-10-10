# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class DbdsPipeline(object):
    def open_spider(self, spider):
        filename = 'e:/dbds.json'
        self.jsonfile = open(filename, 'w')
        self.jsonfile.write('[\n')

    def process_item(self, item, spider):
        self.jsonfile.write(json.dumps('[NEW]'))
        self.jsonfile.write(json.dumps(dict(item)) + ',\n')
        return item

    def close_spider(self, spider):
        if self.jsonfile:
            self.jsonfile.write(']')
            self.jsonfile.close()