# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# Create the lyics item with an artist, url and text
# You might consider adding an entry for song name -- how would you do that?
class LyricsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    artist = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()

