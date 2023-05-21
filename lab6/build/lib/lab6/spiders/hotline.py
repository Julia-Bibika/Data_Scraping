import scrapy
from bs4 import BeautifulSoup
from lab6.items import HotlineItem

class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/musical_instruments/gitary-akusticheskie/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")

        items = soup.find(
            name="div", class_="list-body__content").find_all(class_="list-item")
        for item in items:
            name = item.find(name="a", class_="list-item__title").find(
                string=True, recursive=False).strip()
            url_instrument = item.find(name="a", class_="list-item__title").get("href")
            price = item.find(class_="price__value").find(
                string=True, recursive=False)
            image_url = item.find(name="img").get("src")
            yield HotlineItem(
                name=name,
                price=price,
                url=url_instrument,
                image_urls=[f"https://hotline.ua{image_url}"]
            )
