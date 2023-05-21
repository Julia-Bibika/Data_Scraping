import scrapy
from bs4 import BeautifulSoup
from lab6.items import RozetkaItem

class RozetkaSpider(scrapy.Spider):
    name = "rozetka"
    allowed_domains = ["rozetka.com.ua"]
    start_urls = ["https://rozetka.com.ua/all-tv/c80037/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="layout_with_sidebar").find_all(class_="goods-tile__inner")
        for item in items:
            name = item.find(name="span", class_="goods-tile__title").find(
                string=True, recursive=False).strip()
            url_instrument = item.find(name="a", class_="goods-tile__heading").get("href")
            price = item.find(name = "span",class_="goods-tile__price-value").find(
                string=True, recursive=False)
            image_url = item.find(name="img" ,class_ ="ng-lazyloaded").get("src")
            yield RozetkaItem(
                name=name,
                price=price,
                url=url_instrument,
                image_urls=image_url
            )
