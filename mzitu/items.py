# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituItem(scrapy.Item):
    # 套图名字
    name = scrapy.Field()
    # 图片地址
    image_urls = scrapy.Field()
    # 请求时的路径, 用于请求头referer防盗链的伪装
    url = scrapy.Field()
    pass

