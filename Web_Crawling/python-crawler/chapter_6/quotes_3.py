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
        for i, quote_html in enumerate(response.css('div.quote')):
            # 테스트로 3개만 추출해봅니다.
            if i > 2:
                raise scrapy.exceptions.CloseSpider(reason='abort')
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            yield item
