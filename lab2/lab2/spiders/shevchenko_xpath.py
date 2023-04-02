import scrapy
from lab2.items import FacultyItem, DepartmentItem


class ShevchenkoXpathSpider(scrapy.Spider):
    name = "shevchenko_xpath"
    allowed_domains = ["www.univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments/"]

    def parse(self, response):
        fac_list = response.xpath('//ul[contains(@class,"b-references__holder")]').xpath('.//li[contains(@class,"b-references__item")]')
        for faculty in fac_list:
            fac_name = faculty.xpath('.//a[contains(@class,"b-references__link")]/text()').get()
            fac_url = faculty.xpath('.//a[contains(@class,"b-references__link")]/@href()').get()
            yield FacultyItem(
                name=fac_name,
                url="http://www.univ.kiev.ua" + fac_url
                )
            yield scrapy.Request(               
                    url="http://www.univ.kiev.ua" + fac_url,
                    callback=self.parse_faculty,
                    meta={
                        "faculty": fac_name
                    }
                )
    # def parse_faculty(self, response):
    #             dep_list = response.xpath('ol').xpath('.b-body__text')
    #             for li in dep_list:
    #                 dep_name = li.xpath('//li[contains(@class,"b-body__text")]/text()').get()
    #                 if dep_name == None:
    #                         dep_name = li.xpath('//a[contains(@class,"b-body__link")]/text()').get()

    #                 dep_url = li.xpath('//a[contains(@class,"b-body__link")]/@href()').get()
                              
    #                 yield DepartmentItem(
    #                     name=dep_name,
    #                     url = dep_url ,
    #                     faculty=response.meta.get("faculty")
    #                     )