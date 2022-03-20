import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags, replace_escape_chars, strip_html5_whitespace
from scrapy.item import Item

def cleaning_description(text):
    return text.replace("\u00ae", " ").replace("\xa0", " ")

class GDLPItem(Item):
    product = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, strip_html5_whitespace), output_processor=TakeFirst())
    url = scrapy.Field(input_processor=MapCompose(strip_html5_whitespace), output_processor=TakeFirst())
    description = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace))
    genre = scrapy.Field()
    product_info = scrapy.Field()
    sku = scrapy.Field(input_processor=MapCompose(remove_tags, replace_escape_chars, cleaning_description, strip_html5_whitespace), output_processor=TakeFirst())
    image_uris = scrapy.Field()
    image_urls = scrapy.Field()
    reference_first_image = scrapy.Field(output_processor=TakeFirst())
    timestamp = scrapy.Field()
    sizes_and_stock = scrapy.Field()
    spider = scrapy.Field(output_processor=TakeFirst())
    spider_version = scrapy.Field(output_processor=TakeFirst())