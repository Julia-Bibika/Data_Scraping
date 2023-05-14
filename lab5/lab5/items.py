# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DinamicItem(scrapy.Item):
    url = scrapy.Field()
    image_urls = scrapy.Field()
