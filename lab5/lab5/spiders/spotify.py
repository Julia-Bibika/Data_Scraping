import scrapy
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from lab5.items import DinamicItem

class SpotifySpider(scrapy.Spider):
    name = "spotify"
    allowed_domains = ["open.spotify.com"]
    start_urls = ["http://open.spotify.com/"]

    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
            )
    def parse(self, response):
        for img in response.css("div.g4PZpjkqEh5g7xDpCr2K"):
            url = img.css("img.SKJSok3LfyedjZjujmFt").css('::attr(src)').get()
            yield DinamicItem(
                url=url,
                image_urls=[url],
            )