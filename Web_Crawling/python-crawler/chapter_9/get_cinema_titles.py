"""크롬 헤드리스 드라이버로 자바스크립트를 사용하는 페이지 스크레이핑하기"""
import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 로거 설정
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '[%(levelname)s] %(asctime)s %(name)s %(filename)s:%(lineno)d %(message)s'
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# 크롬드라이버 실행 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/
MacOS/Google Chrome'
chrome_driver_path = ('/Users/hasat/python/chromedriver')

if __name__ == '__main__':
    try:
        # 크롬을 헤드리스 모드로 실행
        driver = webdriver.Chrome(chrome_driver_path, chrome_options=chrome_options)

        # 스크레이핑 대상 URL 지정
        target_url = "http://0.0.0.0:8000/vue_sample.html"
        # 헤드리스 모드 크롬으로 스크레이핑 대상 페이지 열기
        driver.get(target_url)

        # 내부적으로 Ajax를 사용해서 처리하는 경우
        # 화면을 모두 읽어 들일 때까지 어느 정도 대기해야 합니다.
        time.sleep(2)

        # 영화 제목 요소를 CSS 선택자로 지정해서 추출합니다.
        title_elms = driver.find_elements_by_css_selector(".cinema_title")

        # 추출된 요소를 출력합니다.
        for i, t in enumerate(title_elms):
            print(i+1, t.text)
    except Exception as e:
        # 예외가 발생했을 경우 스택 트레이스를 출력합니다.
        logger.exception(e)
    finally:
        # 예외가 발생해서 프로그램이 종료됐을 때
        # 크롬 프로세스가 남는 것을 피할 수 있게 finally 구문 내부에서 종료해줍니다.
        driver.close()
