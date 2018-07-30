# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mzitu.items import MzituItem


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/']
    img_urls = [] # 要把图片放到一个列表方便pipeline使用
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.mzitu.com/\d{4,6}',), deny='http://www.mzitu.com/\d{1,6}/\d{1,6}'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MzituItem()
        # max_num为页面最后一张图片的位置
        max_num = response.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()').extract_first(default="N/A")
        item['name'] = response.xpath('//div[@class="content"]/h2/text()').extract_first(default="N/A")
        item['url'] = response.url
        for num in range(1, int(max_num)):
            # page_url 为每张图片所在的页面地址
            page_url = response.url + '/' + str(num)
            yield scrapy.Request(page_url, callback=self.img_url)
        item['image_urls'] = self.img_urls
        yield item

    def img_url(self, response,):
        img_urls = response.xpath('//div[@class="main-image"]//a/img/@src').extract()
        for img_url in img_urls: # 每张图片的真实地址
            self.img_urls.append(img_url)


















