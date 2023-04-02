# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector
import sqlite3
from scrapy.exceptions import DropItem

class SqlitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect("items.db")
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to Sqlite ")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        items (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT NOT NULL,
            price FLOAT DEFAULT 0,
            url TEXT
        );""")
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from Sqlite ")

    def process_item(self, item, spider):
        if self.is_duplicate(item):
            self.cursor.execute("""
                                    UPDATE items
                                    SET price = ?
                                    WHERE name = ?
                                    """,
                                [item.get("price"), item.get("name")]
                                )
        else:
            self.cursor.execute(
                "INSERT INTO items (name, price, url) VALUES (?, ?, ?);",
                [item.get("name"), item.get("price"), item.get("url")])

        self.connection.commit()
        return item

    def is_duplicate(self, item):
        self.cursor.execute(
            "SELECT COUNT(id) FROM items WHERE name = ?;",
            [item.get("name")])
        count = self.cursor.fetchone()[0]
        return count > 0


class MySqlPipeline:
    def open_spider(self, spider):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="scrapy"
        )
        self.cursor = self.connection.cursor()
        spider.logger.info("Connected to MySQL ")
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS 
        items (
            id INT AUTO_INCREMENT,
            PRIMARY KEY (id),
            name VARCHAR(50) NOT NULL,
            price FLOAT DEFAULT 0,
            url VARCHAR(500)
        );""")
        spider.logger.info("DB is ready ")

    def close_spider(self, spider):
        self.connection.close()
        spider.logger.info("Disconnected from MySQL ")

    def process_item(self, item, spider):
        if self.is_duplicate(item):
            self.cursor.execute("""
                                    UPDATE items
                                    SET price = %s
                                    WHERE name = %s
                                    """,
                                [item.get("price"), item.get("name")]
                                )
        else:
            self.cursor.execute(
                "INSERT INTO items (name, price, url) VALUES (%s, %s, %s);",
                [item.get("name"), item.get("price"), item.get("url")])

        self.connection.commit()
        return item

    def is_duplicate(self, item):
        self.cursor.execute(
            "SELECT COUNT(id) FROM items WHERE name = %s;",
            [item.get("name")])
        count = self.cursor.fetchone()[0]
        return count > 0
    
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
