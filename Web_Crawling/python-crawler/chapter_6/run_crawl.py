"""scrapy의 quotes 크롤러 호출하기"""
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def run_crawl():
    """크롤링 실행"""
    process = CrawlerProcess(get_project_settings())
    process.crawl('quotes')
    process.start()
    
if __name__ == '__main__':
    run_crawl()