# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FacultyItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
class DepartmentItem(scrapy.Item):
    name = scrapy.Field()
    faculty = scrapy.Field()
    url = scrapy.Field()
class StaffItem(scrapy.Item):
    name = scrapy.Field()
    department = scrapy.Field()