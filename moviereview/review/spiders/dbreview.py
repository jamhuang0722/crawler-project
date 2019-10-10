# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import ReviewItem


class DbreviewSpider(RedisCrawlSpider):
    name = 'dbreview'
    allowed_domains = ['douban.com']
    redis_key = 'dbreview:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        comments = response.xpath('//div[@class="comment"]//span[@class="short"]/text()').extract()
        for comment in comments:
            item = ReviewItem()
            item['review'] = comment.strip()
            print(item)
            yield item
