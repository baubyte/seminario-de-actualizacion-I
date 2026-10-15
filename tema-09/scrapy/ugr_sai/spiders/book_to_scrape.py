from datetime import datetime
import logging
from typing import Union

from scrapy import Spider
from scrapy.http.request import Request
from scrapy.http.response import Response

from ugr_sai.items import Book
from ugr_sai.loaders import BookLoader


# http://books.toscrape.com/
class BooksSpider(Spider):

    name = "books"
    # overwrite default settings
    custom_settings = {
        "ITEM_PIPELINES": {
            "ugr_sai.pipelines.FixDataPipeline": 100,
            "ugr_sai.pipelines.LogPipeline": 200
        },
        "FEED_FORMAT": "json",
        "FEED_URI": "/opt/project/downloads/books.json"
    }

    def start_requests(self) -> Request:
        """ Start request.

        Yields:
            Request: Return one object Request to analyze.
        """
        urls = [
            "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
            "http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html",
            "http://books.toscrape.com/catalogue/soumission_998/index.html",
            "http://books.toscrape.com/catalogue/sharp-objects_997/index.html",
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response: Response) -> Union[None, Book]:
        """ Parse the response.

        Args:
            response (Response): Response object.

        Returns:
            Union[None, Book]: Return an item Book or None.

        Yields:
            Iterator[Union[None, Book]]: Return an item of type Book to the next pipelines step.
        """
        if response is not None:
            # initialize BookLoader and Book
            bookLoader = BookLoader(item=Book(), response=response)
            # mapping properties and sources
            bookLoader.add_xpath("name", "//article/div/div/h1/text()")
            bookLoader.add_css("currency", ".price_color::text")
            bookLoader.add_css("availability", ".availability::text")
            bookLoader.add_xpath("description", "//article/p/text()")
            bookLoader.add_value(
                "last_updated",
                datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))
            # fill the item Book
            book: Book = bookLoader.load_item()

            yield book
        else:
            self.log(f'Error', logging.ERROR)
