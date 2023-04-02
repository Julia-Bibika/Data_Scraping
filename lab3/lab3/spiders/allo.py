import scrapy
from bs4 import BeautifulSoup
from lab3.items import PhoneItem

class AlloSpider(scrapy.Spider):
    name = "allo"
    allowed_domains = ["allo.ua"]
    start_urls = ["https://allo.ua/ua/products/mobile/klass-kommunikator_smartfon/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="products-layout__container").find_all(class_="products-layout__item")
        for item in items:
            name = item.find(name="a", class_="product-card__title").find(
                string=True, recursive=False).strip()
            url = item.find(name="a", class_="product-card__title").get("href")
            price = item.find(name = "span",class_="sum").find(
                string=True, recursive=False)
            image_url = item.find(name="img",class_="gallery__img").get("src")

            yield PhoneItem(
                name=name,
                price=price,
                url=url,
                image_urls=[image_url]
            )
