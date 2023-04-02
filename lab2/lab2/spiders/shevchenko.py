import scrapy
from bs4 import BeautifulSoup
from lab2.items import FacultyItem, DepartmentItem,StaffItem

class ShevchenkoSpider(scrapy.Spider):
    name = "shevchenko"
    allowed_domains = ["www.univ.kiev.ua"]
    start_urls = ["http://www.univ.kiev.ua/ua/departments/"]

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        fac_list = soup.find(class_="b-references__holder")
        for li in fac_list.find_all("li"):
            a = li.find("a")
            fac_name = a.find(string=True, recursive=False)
            fac_url = a.get('href')
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
    def parse_faculty(self, response):
                soup = BeautifulSoup(response.body,  "html.parser")
                dep_list = soup.find(class_="b-body__holder")
                li_list = dep_list.find("ol")
                if li_list:
                    for li in li_list.find_all("li"):
                        dep_name = li.find(string=True, recursive=False)
                        if dep_name == None:
                            dep_name = li.a.find(string=True, recursive=False)
                        dep_url = li.a.get('href')
                              
                        yield DepartmentItem(
                            name=dep_name,
                            url = dep_url ,
                            faculty=response.meta.get("faculty")
                        )
#                         yield scrapy.Request(
#                         url=dep_url+"vikladachi/",
#                         callback=self.parse_department,
#                         meta={
#                             "department": dep_name
#                         }
#                     )
# def parse_department(self, response):
#         soup = BeautifulSoup(response.body,  "html.parser")
#         staff_list = soup.find(class_ = "entry-content wow fadeInUp")
#         if staff_list:
#             for h3 in staff_list.find_all("h3"):
#                 name = h3.find(string=True, recursive=False)
#                 yield StaffItem(
#                     name=name,
#                     department=response.meta.get("department")
#                 )