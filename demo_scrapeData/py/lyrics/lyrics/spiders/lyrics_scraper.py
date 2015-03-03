# -*- coding: utf-8 -*-

# Define your item pipelines here
# We have no item pipelines, refer to settings.py to see how we deal with exporting data

# Import statements
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
import string
from lyrics.items import LyricsItem
import time

#class LyricsScraper(scrapy.Spider):
class LyricsScraper(CrawlSpider):
    # Give your scraper a name!
    name = "lyrics"
    
    # Your scraper will only visit domains that are allowed (here)
    allowed_domains = ["billboard.com","genius.com","country.genius.com"]
    
    # This is where your scraper will start
    start_urls = [ "http://www.billboard.com/charts/year-end/2014/top-country-artists"]
    
    # Optional setting, we will leave empty
    rules = ()
    
    # Parse the page containing the lyrics for each song
    # Note we use LyricsItem which we have defined in lyrics/items.py
    # We use an xpath to find the appropriate part of the webpage, extract its value and save
    # Finally yield the item so it can be saved as output
    def parse_lyricsPage(self,response):
        item = LyricsItem()
        item['artist']=response.xpath('//*[@class="text_artist"]/a/text()').extract()
        item['text']=response.xpath('//*[@class="lyrics_container"]/div/p/a/text()').extract()
        yield item

    
    # Parse the page containing all the names of the songs by an artist and containing links to lyrics pages.
    # For each link, we create a new request to visit and parse that page using parse_lyricsPage
    # Note that we sleep two seconds after each query to avoid slamming their system
    def parse_artistPage(self,response):
        for link in response.xpath('//*[@id="main"]/ul/li/a/@href').extract():
            request = Request(link,callback=self.parse_lyricsPage)
            time.sleep(2)
            yield request

    
    # Parse the starting url, which is a billboard page of top country artists for 2014
    # For this parser, we will describe each step in detail
    def parse_start_url(self, response):
        # We know the xpath that gets all the artist names -- put them in a list
        namesList = response.xpath('//a[@trackaction="Artist Name"]/text()').extract()
        # Go through each artist name in the list one by one
        for artistName in namesList:
            # Similar to the text cleaning we've done before
            # Remove new line and tab characters, punctuation, spaces and all upper case letters in names
            # Uncomment the print statement below to see how messy the names are before this cleaning
            # print artistName
            artistName = artistName.strip()
            artistName = artistName.encode('utf-8').translate(None, string.punctuation)
            artistName = artistName.replace(" ","+")
            artistName = artistName.lower()
            # Construct a new URL, using our knowledge of how the Country Genius website formulates URLs for queries (ie. for searches)
            # Note this has potential dangers: if we search, we may be getting pages back that are not exact matches. Look through the results to see if you can identify this happening.
            newURL = "http://genius.com/search?q=" + artistName
            # If you scrape a website too frequently, it is considered rude. You also may be blocked.
            # To avoid scraping too frequently, we sleep for two seconds between each query.
            time.sleep(2)
            # The way that scrapy handles scraping a new page is through requests. You create a request to visit the URL you are interested in (likely one you scraped off this page) and assign a callback (or function) you want to use to parse the new URL. Then yield that request.
            request = Request(newURL,callback=self.parse_artistPage)
            yield request

