from requests import get
from bs4 import BeautifulSoup
BASE_URL="http://www.univ.kiev.ua"
URL = f"{BASE_URL}/ua/departments"
HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "lab1.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:
    page = get(URL, headers=HEADERS)
    soup = BeautifulSoup(page.content,  "html.parser")
    fac_list = soup.find(class_="b-references__holder")
    for li in fac_list.find_all("li"):
        a = li.find("a")
        fac_name = a.find(string=True, recursive=False)
        fac_link = BASE_URL+ a.get("href")
        print(f"Назва факультету: {fac_name}")
        print(f"URL: {fac_link}")
        file.write(f"Назва факультету: {fac_name}\n")
        file.write(f"URL: {fac_link}\n")

    fac_page = get(fac_link, headers=HEADERS)
    soup = BeautifulSoup(fac_page.content,  "html.parser")
    dep_list = soup.find(class_="b-body__holder")
    li_list = dep_list.find("ol")
    for li in li_list.find_all("li"):
        dep_name = li.find(string=True, recursive=False)
        print(f"    Назва кафедри: {dep_name}")
        file.write(f"Назва кафедри: {dep_name}\n")
