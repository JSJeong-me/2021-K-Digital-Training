"""격언 스크레이핑 프로그램"""
import scrapy

class Quote(scrapy.Item):
    """격언 아이템"""
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()