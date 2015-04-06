# -*- coding: utf-8 -*-

# Scrapy settings for olympics project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'olympics'

SPIDER_MODULES = ['olympics.spiders']
NEWSPIDER_MODULE = 'olympics.spiders'

CONCURRENT_REQUESTS = 1

# Export Information
# Tell it to export in Json Lines format, to the res folder
FEDD_EXPORTERS = {'jsonlines': 'scrapy.contrib.exporter.JsonLinesItemExporter',}
FEED_FORMAT = 'jsonlines'
FEED_URI = 'file:../../../../res/olympics.json'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'olympics (+http://www.yourdomain.com)'
