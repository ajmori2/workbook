# -*- coding: utf-8 -*-

# Scrapy settings for lyrics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

# Basic name information and limit to one concurrent request (scraping nicely)
BOT_NAME = 'lyrics'
SPIDER_MODULES = ['lyrics.spiders']
NEWSPIDER_MODULE = 'lyrics.spiders'
CONCURRENT_REQUESTS = 1

# Export Information
# Tell it to export in Json Lines format, to the res folder
FEDD_EXPORTERS = {'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',}
FEED_FORMAT = 'jsonlines'
FEED_URI = 'file:../../../../res/lyrics.json'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lyrics (+http://www.yourdomain.com)'
