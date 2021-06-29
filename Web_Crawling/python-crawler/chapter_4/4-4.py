import feedparser

# URL을 지정해서 FeedParserDict 객체를 생성합니다.
rss = feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")

# RSS의 버전을 출력합니다.
print(rss.version)

# 피드의 타이틀과 콘텐츠의 생성 날짜를 출력합니다.
print(rss["feed"]["title"])

# 엔트리들의 제목과 링크를 출력합니다.
for content in rss["entries"]:
    print(content["title"])
    print(content["link"])
