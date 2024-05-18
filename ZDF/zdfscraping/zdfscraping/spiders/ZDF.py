from typing import Any

import scrapy


class ZDF(scrapy.Spider):
    name = "zdf_scrapy"
    start_urls = ["https://www.zdf.de/nachrichten"]

    def parse(self, response):
        for link in [response.urljoin(sublink) for sublink in response.css("div.i13b5qgu a ::attr(href)").extract()]:
            yield response.follow(link, callback=self.linkToNews)

    def linkToNews(self, response):
        for link in [response.urljoin(sublink) for sublink in response.css('a.f1mro3s7.sn98z8j._nl_::attr(href)').extract()]:
            yield response.follow(link, callback=self.getNews)

    def getNews(self, response):
        yield {
            "Link": response,
            "News Category" : response.css('span.o1byiadb.t1ktg2ut ::text').extract(),
            "publish_time": response.css('span.djkus7a.m211382 ::text').extract(),
            "Title" : response.css('span.t1w1kov8.hhhtovw ::text').extract(),
            "scribe": response.css('p.ikh9v7p.c1bdz7f4 ::text').extract(),
            "Text": response.css('div.s1am5zo.f1uhhdhr ::text').extract()
        }

