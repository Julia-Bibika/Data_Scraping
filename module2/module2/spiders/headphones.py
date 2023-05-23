import scrapy


class HeadphonesSpider(scrapy.Spider):
    name = "headphones"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/239/{page}/" for page in range(1,5)]

    def parse(self, response):
        pass
