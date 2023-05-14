import scrapy
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 

class TwitterSpider(scrapy.Spider):
    name = "twitter"
    allowed_domains = ["twitter.com"]
    start_urls = ["https://twitter.com/i/connect_people?user_id=1650414646451421185"]

    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10,
                wait_until=expected_conditions.element_to_be_clickable(
                   (By.CSS_SELECTOR,
                    "div img")
                ),
                execute=self.login
            )

    def login(self, driver, wait):
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, '//input[@name="name"]')))
        name_input = driver.find_element(By.XPATH, '//input[@name="name"]')
        name_input.send_keys("NameTest")
        username_email = driver.find_element(By.XPATH, '//input[@name="email"]')
        username_email.send_keys("EmailTest@gmail.com")   
        login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Не зараз')]")))
        later_button = driver.find_element(By.XPATH, "//button[contains(text(),'Не зараз')]")
        later_button.click()


            
    def parse(self, response):
        pass
