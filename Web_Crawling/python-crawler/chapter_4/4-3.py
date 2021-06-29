import requests
import lxml.html
# HTML 소스 코드를 읽어 들입니다.
r = requests.get("http://wikibook.co.kr/python-for-web-scraping/")
html = r.text

# HTML을 HtmlElement 객체로 변환합니다.
root = lxml.html.fromstring(html)

# XPath를 사용해서 요소를 추출합니다.
titleElement = root.xpath('//*[@id="content"]/div[1]/div[2]/ul/li[1]')

# 리스트의 첫 번째 요소가 가진 텍스트를 출력합니다.
print(titleElement[0].text)

# CSS 선택자를 사용해서 요소를 추출합니다.
linkAs = root.cssselect('#book-stores > li > a')

## for 반복문으로 추출한 요소의 href 속성을 추출합니다.
for linkA in linkAs:
    print(linkA.attrib["href"])
