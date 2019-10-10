# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.http import HtmlResponse
from ..items import BookItem


class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?start=0&type=T']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response:HtmlResponse):
        for subject in response.xpath('//li[@class="subject-item"]'):
            item = BookItem()

            title = subject.xpath('.//h2/a//text()')
            item['title'] = ''.join(map(lambda x:x.strip(), title.extract()))

            rate = subject.xpath('.//span[@class="rating_nums"]/text()')
            rate2 = rate.extract()[0]
            item['rate'] = rate.extract_first()[0] if rate else '0'
            # print(dict(item))
            yield item
