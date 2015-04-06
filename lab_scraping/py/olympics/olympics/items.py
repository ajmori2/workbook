# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OlympicsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    event = scrapy.Field()
    athlete = scrapy.Field()
    result = scrapy.Field()
    pass
