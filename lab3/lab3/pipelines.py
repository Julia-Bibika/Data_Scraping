# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
from scrapy.exceptions import DropItem

from lab3.items import PhoneItem

class Lab3Pipeline:
    def process_item(self, item, spider):
        if isinstance(item, PhoneItem):
            item["name"] = item.get("name") + "."
            item["url"] = item.get("url")
        return item

class SQLPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="laravel"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            name VARCHAR(64),
            price VARCHAR(1024),
            url VARCHAR(1024)
        );
        """)
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if isinstance(item, PhoneItem):
            self.cursor.execute(
                "INSERT INTO items (name, price, url) VALUES (%s, %s, %s);",
                [item.get("name"), item.get("price"), item.get("url")]
            )
            self.connection.commit()
        return item
    
class PricePipeline:
    def process_item(self, item, spider):
        try:
            item["price"] = float(item.get("price").replace("&nbsp;", ""))
            return item
        except:
            raise DropItem(f"Bad price in {item}")
class FilterPipeline:
    def filter(self, item):
        return "Apple" in item.get("name")

    def process_item(self, item, spider):
        if self.filter(item):
            raise DropItem(f"Item {item} by filter")
        return item
