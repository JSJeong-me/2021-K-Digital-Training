import time

import requests

PAGE_URL_LIST = [
    'http://example.com/1.page',
    'http://example.com/2.page',
    'http://example.com/3.page',
]

for page_url in PAGE_URL_LIST:
    res = requests.get(page_url, timeout=30)
    print(
        "페이지 URL:{}, HTTP 상태: {}, 처리 시간(초): {}".format(
            page_url,
            res.status_code,
            res.elapsed.total_seconds()
        )
    )
    time.sleep(1)
