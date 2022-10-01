# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log(f'got response from {response.url}')

        quotes = response.css('.quote')
        for quote in quotes:
            item ={
                'author':quote.css('.author::text').get(),
                'quote':quote.css('.text::text').get(),
                'tags':quote.css('.tag::text').getall()
            }
            yield item



        # item ={
        #     'Author':response.css('.author::text').get(),
        #     'Quote' :response.css('.text::text').get(),
        #     'tags' :response.css('.tag::text').getall()
        # }
        # yield item