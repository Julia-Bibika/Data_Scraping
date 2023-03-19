import scrapy
from lab2.items import FacultyItem, DepartmentItem

class ShevchenkoCssSpider(scrapy.Spider):
    name = "shevchenko_css"
    allowed_domains = ["www.univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments"]

    def parse(self, response):
        fac_list = response.css('ul.b-references__holder').css('li.b-references__item')
        for faculty in fac_list:
            fac_name = faculty.css('a.b-references__link::text').get()
            fac_url = faculty.css('a.b-references__link::attr(href)').get()
            yield FacultyItem(
                name=fac_name,
                url="http://www.univ.kiev.ua" + fac_url
                )
            yield scrapy.Request(               
                    url=fac_url,
                    callback=self.parse_faculty,
                    meta={
                        "faculty": fac_name
                    }
            )
    def parse_faculty(self, response):
                dep_list = response.css('ol').css('.b-body__text')
                for li in dep_list:
                    dep_name = li.css("li.b-body__text::text").get()
                    if dep_name == None:
                            dep_name = li.css("a.b-body__link::text").get()

                    dep_url = li.css("a.b-body__link::attr(href)").get()
                              
                    yield DepartmentItem(
                        name=dep_name,
                        url = dep_url ,
                        faculty=response.meta.get("faculty")
                        )
