import scrapy
from module2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from module2.items import HeadPhoneItem

class HeadphonesSpider(scrapy.Spider):
    name = "headphones"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/239/{page}/" for page in range(1,7)]

    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
            )
    def parse(self, response):
        items = response.css("form#list_form1").css("div.list-item--goods")
        for item in items:
            name = item.css('span.u::text').get()
            url = item.css('div.list-zoomer').css('img#img_he8e82apjye::attr(href)').get()
            shops = item.css("table.model-hot-prices").css("tr")
            for shop in shops:
                shop_name = shop.css('a').css('u::text').get()
                price_product = item.css('td.model-shop-price').css('a::text').get()
        yield HeadPhoneItem(
                name_product = name,
                img_url = url,
                shop = [shop_name],
                price = [price_product],
            )