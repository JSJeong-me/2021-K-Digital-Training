import pytest

from scraper import ScraperException, scrape_title

def test_scraper_title():
    html = """<html>
    <title>제목</title>
    <body><p>내용입니다.</p></body>
    </html>"""

    assert scrape_title(html) == "제목"

    html_without_title = """<html>
    <body><p>내용입니다.</p></body>
    </html>"""

    with pytest.raises(ScraperException) as e:
        scrape_title(html_without_title)
        assert 'title 태그가 존재하지 않습니다.' == e.value

    html_empty_title = """<html>
    <title></title>
    <body><p>내용입니다.</p></body>
    </html>"""

    with pytest.raises(ScraperException) as e:
        scrape_title(html_empty_title)
        assert 'title 태그에 내용이 없습니다.' == e.value
