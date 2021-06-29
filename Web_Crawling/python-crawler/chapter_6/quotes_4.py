"""http://quotes.toscrape.com/ 크롤러
하나 아래 계층까지 크롤링해서 페이지마다 격언을 1개씩 수집합니다.
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from my_project.items import Quote

class QuotesSpider(CrawlSpider):
    """Quote 아이템을 수집하는 크롤러"""

    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    
    rules = (
        Rule(
            LinkExtractor(allow=r'.*'),
            callback='parse_start_url',
            follow=True,
        ),
    )

    def parse_start_url(self, response):
        """start_urls 아래의 다른 페이지도 스크레이핑합니다."""
        return self.parse_item(response)

    def parse_item(self, response):
        """크롤링한 페이지에서 Item을 스크레이핑합니다."""
        # 한 페이지에서 1개의 아이템만 수집합니다.
        items = []
        for i, quote_html in enumerate(response.css('div.quote')):
            # 테스트로 1개만 추출해봅니다.
            if i > 1:
                return items
            item = Quote()
            item['author'] = quote_html.css('small.author::text').extract_first()
            item['text'] = quote_html.css('span.text::text').extract_first()
            item['tags'] = quote_html.css('div.tags a.tag::text').extract()
            items.append(item)
