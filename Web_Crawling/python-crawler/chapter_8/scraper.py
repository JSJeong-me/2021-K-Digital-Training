from bs4 import BeautifulSoup

class ScraperException(Exception):
    """스크레이핑 예외"""

def scrape_title(html):
    """<title> 태그의 내용을 반환합니다."""
    soup = BeautifulSoup(html, "html.parser")
    title_elm = soup.find('titel')
    if title_elm is None:
        raise ScraperException('title 태그가 존재하지 않습니다.')
    title = title_elm.text
    if not title:
        raise ScraperException('title 태그에 내용이 없습니다.')
    return title_elm.text
