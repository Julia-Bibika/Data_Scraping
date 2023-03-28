# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
class ShopItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()