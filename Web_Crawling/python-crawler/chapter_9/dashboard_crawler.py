"""Tumblr 대시보드를 크롤링합니다."""
import json
import pytumblr

# OAuth 인증을 사용한 API 클라이언트 객체를 생성합니다.
client = pytumblr.TumblrRestClient(
    # 아래 부분은 샘플 코드 부분을 복사해서 사용해주세요.
    'XXXXXXXXXX',
    'XXXXXXXXXX',
    'XXXXXXXXXX',
    'XXXXXXXXXX'
)

def get_dashboard_posts():
    """대시보드의 글 추출하기"""
    return client.dashboard(type='text')

if __name__ == '__main__':
    dashboard_posts = get_dashboard_posts()
    print(json.dumps(dashboard_posts, ensure_ascii=False))