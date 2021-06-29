import json
import time

import requests

# 크롤링 대상 URL 리스트
PAGE_URL_LIST = [
    'http://example.com/1.page'
    'http://example.com/2.page',
    'http://example.com/3.page',
]

def fetch_pages():
    """페이지의 내용을 추출합니다"""
    # 처리 기록 전용 로그 파일을 append 모드로 엽니다
    f_info_log = open('crawler_info.log', 'a')

    # 오류 기록 전용 로그 파일을 append 모드로 엽니다
    f_error_log = open('crawler_error.log', 'a')

    # 추출 내용을 저장할 딕셔너리
    page_contents = {}

    # 터미널에 처리 시작을 출력하고, 로그 파일에도 메시지를 출력합니다.
    msg = "크롤링을 시작합니다\n"
    print(msg)
    f_info_log.write(msg)

    for page_url in PAGE_URL_LIST:
        r = requests.get(page_url, timeout=30)
        try:
            r.raise_for_status()  # 응답에 문제가 있으면 예외를 발생시킵니다.
        except requests.exceptions.RequestException as e:
            # requests와 관련된 예외가 발생하면
            # 터미널과 오류 로그에 오류를 출력합니다.
            msg = "[ERROR] {exception}\n".format(exception=e)
            print(msg)
            f_error_log.write(msg)
            continue  # 예외가 발생하면 반복을 중지하는게 아니라 건너 뜁니다.
        # 정상적으로 내용을 추출했다면 딕셔너리에 내용을 저장합니다.
        page_contents[page_url] = r.text
        time.sleep(1)  # 상대 사이트에 대한 부하를 고려해서 요청 간격을 설정합니다.

    f_info_log.close()
    f_error_log.close()

    return page_contents

if __name__ == '__main__':
    page_contents = fetch_pages()
    f_page_contents = open('page_contents.json', 'w')
    json.dump(page_contents, f_page_contents, ensure_ascii=False)
    f_page_contents.close()
