import scrapy
from bs4 import BeautifulSoup
from lab7.items import ShopItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = [f"https://hotline.ua/ua/mobile/mobilnye-telefony-i-smartfony/?p={page}" for page in range(1, 8)]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")
        for item in items:
            url_phone = item.find(name="a", class_="list-item__title").get("href")
            yield scrapy.Request(
                url="https://hotline.ua" + url_phone,
                callback=self.parse_shop,
             )
    def parse_shop(self, response):
                soup = BeautifulSoup(response.body,  "html.parser")
                name = soup.find(name='h1',class_='title__main').find(string=True, recursive=False)

                shop = soup.find(name="div", class_="list").find(class_="list__item")
                shop_name = shop.find(name="a", class_="shop__title").find(string=True, recursive=False).strip()
                price_product = shop.find(name='span' , class_='price__value').find(string=True, recursive=False)
                yield ShopItem(
                    name=shop_name,
                    name_product = name,
                    price = price_product,
                )
