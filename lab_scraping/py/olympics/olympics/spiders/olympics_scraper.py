# -*- coding: utf-8 -*-

# Define your item pipelines here
# We have no item pipelines, refer to settings.py to see how we deal with exporting data

# Import statements
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
import string
from olympics.items import OlympicsItem
import time

class OlympicsScraper(CrawlSpider):
    # Give your scraper a name!
    name = "olympics"
    
    # Your scraper will only visit domains that are allowed (here)
    allowed_domains = ["olympic.org"]
    
    # This is where your scraper will start
    # You are given two of the years -- you should figure out how to add the other two Olympics (2000 and 2004)
    start_urls = [ "http://www.olympic.org/olympic-results/london-2012/athletics","http://www.olympic.org/olympic-results/beijing-2008/athletics"]
    
    # Optional setting, we will leave empty
    rules = ()
    
    # You are shown results that will go through and save the men's track and field events. Using this as a model, also save the women's track and field events.
    def parse_start_url(self,response):
        item = OlympicsItem()
        
        # Men's track and field events
        mens_events = response.xpath('//*[@class="block_results"]/span/text()').extract()

        for n in range(len(mens_events)):
            item['event']=mens_events[n]
            mens_athletes = response.xpath('//*[@class="block_results"][' + str(n+1) + ']/table/tr/td/a/text()').extract()
            mens_results = response.xpath('//*[@class="block_results"][' + str(n+1) + ']/table/tr/td/span/text()').extract()
            for j in range(len(mens_results)):
                item['athlete']=mens_athletes[j]
                item['result']=mens_results[j]
                yield item

