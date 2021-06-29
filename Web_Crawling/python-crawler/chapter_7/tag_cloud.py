import requests
from konlpy.tag import Okt
from bs4 import BeautifulSoup
from wordcloud import WordCloud

# HTML 추출하기 : 운수 좋은 날 텍스트
url = 'https://raw.githubusercontent.com/rintiantta/raw-files/master/crawl-cloud-sample.txt'
r = requests.get(url, timeout=10)

# 텍스트 추출
text = r.text

# 형태소 분석
okt = Okt()
words = []
for line in text.split("\n"):
    words.extend(okt.nouns(line))

# wordcloud 객체 생성
# 한국어를 출력할 수 있는 폰트를 지정해야 합니다.
font_path = '/System/Library/Fonts/AppleSDGothicNeo.ttc'
wordcloud = WordCloud(background_color="white", font_path=font_path).generate(" ".join(words))

# 그래프 그리기
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
