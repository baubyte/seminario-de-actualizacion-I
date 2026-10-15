# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import re
# useful for handling different item types with a single interface
from scrapy import Spider

from ugr_sai.items import Book


class LogPipeline:
    """ Class to debug stages. For debugging purposes only. """

    def process_item(self, item: Book, spider: Spider) -> Book:
        """ Process an item

        Args:
            item (Book): Item.
            spider (Spider): Father spider.

        Returns:
            Book: Return an item of type Book.
        """
        spider.log(item, logging.INFO)
        return item


class FixDataPipeline:
    """ Split data:
            - The currency in currency and price
            - The availability in stock
    """

    def process_item(self, item: Book, spider: Spider) -> Book:
        """ Process an item

        Args:
            item (Book): Item.
            spider (Spider): Father spider.

        Returns:
            Book: Return an item of type Book.
        """
        if item["currency"] is not None:
            # split price and currency
            tmp = item["currency"]
            item["currency"] = re.sub(r"[0-9.]+", "", tmp)
            item["price"] = re.sub(r"[^0-9.]+", "", tmp)
        else:
            item["price"] = 0

        if item["availability"] is not None:
            # read the stock quantity
            tmp = item["availability"]
            item["stock"] = re.sub(r"[^0-9.]+", "", tmp)
        else:
            item["stock"] = 0
        return item
