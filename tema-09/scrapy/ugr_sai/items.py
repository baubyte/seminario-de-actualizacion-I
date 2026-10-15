# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from json import dumps
from scrapy import Item, Field


class Book(Item):
    name = Field()
    price = Field()
    currency = Field()
    availability = Field()
    stock = Field()
    description = Field()
    last_updated = Field(serializer=str)

    def __str__(self):
        return dumps({key: self[key]
                      for key in sorted(self.keys())},
                     indent=4,
                     ensure_ascii=False)
