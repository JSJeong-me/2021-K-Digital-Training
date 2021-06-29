# 윈도우에서는 한글 인코딩 오류가 발생할 수 있습니다.
# 한글 인코딩 오류가 발생한다면
# Message.log(message_type="info", msg="데이터를 저장했습니다.")
# 위의 코드 부분의 msg를 영어로 수정해서 사용해주세요.

import json
import sys

from eliot import Message, start_action, to_file, write_traceback
import requests

# 로그 출력을 표준 출력으로 설정(터미널에 출력하기)
to_file(sys.stdout)
# 크롤링 대상 URL 리스트
PAGE_URL_LIST = [
    'https://eliot.readthedocs.io/en/1.0.0/',
    'https://eliot.readthedocs.io/en/1.0.0/generating/index.html',
    'https://example.com/notfound.html',
]
def fetch_pages():
    """페이지의 내용을 추출합니다."""
    # 어떤 처리의 로그인지는 action_type으로 지정
    with start_action(action_type="fetch_pages"):
        page_contents = {}
        for page_url in PAGE_URL_LIST:
            # 어떤 처리의 로그인지 action_type으로 출력
            with start_action(action_type="download", url=page_url):
                try:
                    r = requests.get(page_url, timeout=30)
                    r.raise_for_status()
                except requests.exceptions.RequestException as e:
                    write_traceback()  # 예외가 발생하면 트레이스백 출력
                    continue
                page_contents[page_url] = r.text
        return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    with open('page_contents.json', 'w') as f_page_contents:
        json.dump(page_contents, f_page_contents, ensure_ascii=False)
        
    # 단순하게 로그 메시지만 출력할 수도 있음
    Message.log(message_type="info", msg="데이터를 저장했습니다.")
