import scrapy
from lab4.items import ClockItem 

class ClocksSpider(scrapy.Spider):
    name = "clocks"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/fashion/naruchnye-chasy/"]

    def parse(self, response):
        items = response.css('div.list-body__content').css('.list-item')

        for item in items:
            name = item.css('a.list-item__title::text').get()
            url = item.css('a.list-item__title::attr(href)').get()
            price = item.css('.price__value::text').get()
            image_url = item.css('img::attr(src)').get()
            yield ClockItem(
                name=name,
                price=price,
                url=url,
                image_urls=[f"https://hotline.ua{image_url}"]
            )