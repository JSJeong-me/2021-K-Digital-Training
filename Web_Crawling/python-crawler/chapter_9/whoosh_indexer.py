import os
import sys
import time
import w3lib.html
from dashboard_crawler import get_dashboard_posts
from whoosh_lib import get_or_create_index

if __name__ == '__main__':
    # 인덱스 핸들러 읽어 들이기
    ix = get_or_create_index()

    # 인덱스 쓰기 전용 writer 객체 만들기
    writer = ix.writer()

    # 대시보드의 글 추출하기
    dashboard_posts = get_dashboard_posts()

    # 데이터 인덱싱하기
    for post in dashboard_posts['posts']:
        writer.update_document(
            post_url=post['post_url'],
            # 인덱스 대상 문장에서 HTML 태그 제거하기
            body=w3lib.html.remove_tags(post['body']), 
        )

    # 인덱스 반영하기
    writer.commit()
