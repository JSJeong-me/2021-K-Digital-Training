"""http://quotes.toscrape.com/ 크롤러
메인 페이지만 크롤링해서 격언을 수집합니다.
"""
import scrapy
from scrapy.spiders import CrawlSpider

from my_project.items import Quote

class QuotesSpider(CrawlSpider):
    """Quote 아이템을 수집하는 크롤러"""
    
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        """크롤링한 페이지에서 Item을 스크레이핑합니다."""
        items = []
        for quote_html in response.css('div.quote'):
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            items.append(item)
    return items
