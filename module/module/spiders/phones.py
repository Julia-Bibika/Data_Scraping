import scrapy
from bs4 import BeautifulSoup
from module.items import PhoneItem,ShopItem
class PhonesSpider(scrapy.Spider):
    name = "phones"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/mobile/mobilnye-telefony-i-smartfony/"]
    
    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")
        for item in items:
            name = item.find(name="a", class_="list-item__title").find(
                string=True, recursive=False).strip()
            url_phone = item.find(name="a", class_="list-item__title").get("href")
            price = item.find(class_="price__value").find(
                string=True, recursive=False)
            image_url = item.find(name="img").get("src")
            yield PhoneItem(
                name=name,
                price=price,
                url=url_phone,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
            yield scrapy.Request(
                url="https://hotline.ua" + url_phone,
                callback=self.parse_shop,
             )
    def parse_shop(self, response):
                soup = BeautifulSoup(response.body,  "html.parser")
                shops = soup.find(name="div", class_="list").find_all(class_="list__item")
                for shop in shops:
                    shop_name = shop.find(name="a", class_="shop__title").find(string=True, recursive=False).strip()
                    shop_url = shop.find(name="a", class_="shop__title").get("href")
                              
                    yield ShopItem(
                            name=shop_name,
                            url = shop_url ,
                    )