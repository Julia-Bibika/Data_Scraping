# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
    name = scrapy.Field()
    name_product = scrapy.Field()
    price = scrapy.Field()
