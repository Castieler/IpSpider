# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IpspiderprojectItem(scrapy.Item):
    # define the fields for your item here like:
    ip = scrapy.Field()
    port = scrapy.Field()
    addr = scrapy.Field()
    anon = scrapy.Field()
    type = scrapy.Field()
    sudu = scrapy.Field()
    con_time = scrapy.Field()
    time_online = scrapy.Field()
    validate_time = scrapy.Field()

