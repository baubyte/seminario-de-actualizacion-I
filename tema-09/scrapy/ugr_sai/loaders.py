from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader


def clean_spaces(lines: list) -> str:
    """ Clean spaces.

    Args: 
        lines (list): List of string, every position is a line of the html.

    Returns: 
        str: String with the value.
    """
    return (" ".join([line.strip() for line in lines])).strip()


class BookLoader(ItemLoader):

    default_output_processor = TakeFirst()

    name_in = MapCompose(str.title)

    availability_out = clean_spaces
