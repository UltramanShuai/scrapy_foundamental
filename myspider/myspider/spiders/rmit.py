# -*- coding: utf-8 -*-
import scrapy


class RmitSpider(scrapy.Spider):
    name = 'rmit'
    allowed_domains = ['www.rmit.edu.au']  # 允许爬虫范围
    start_urls = ['https://www.rmit.edu.au']  # 最开始的url

    def parse(self, response):
        # 处理start_url 响应
        # ret1=response.xpath('//div[@class="col-md-12 pagelisting"]//li/a/text()').extract()
        li_list=response.xpath('//div[@class="col-md-12 pagelisting"]//li')

        for li in li_list:
            item={}
            item["name"]=li.xpath(".//a/text()").extract_first()
            item["url"]=li.xpath(".//a/@href").extract_first()

            yield item

