"""feedgen 사용해보기"""
from feedgen.feed import FeedGenerator

# 이전에 만들었던 feedgen_ext에서
# 사용자 정의 네임 스페이스 클래스 읽어 들이기
from feedgen_ext import BookEntryExtension, BookFeedExtension

def create_feed():
    """RSS 피드 생성하기"""

    # 피드 데이터 저장 전용 객체
    fg = FeedGenerator()

    # 사용자 정의 네임 스페이스를 등록하고
    # 이전에 만들었던 클래스 적용하기
    fg.register_extension(
        'book',
        extension_class_feed=BookFeedExtension,
        extension_class_entry=BookEntryExtension,
    )

    # <channel><title> 요소
    fg.title("위키북스의 도서 목록")
    # <channel><link> 요소: <link> 태그의 내용은 href 속성으로 지정
    fg.link(href="http://example.com")
    # <channel><description> 요소
    fg.description("설명을 입력했다고 가정합니다.")

    # <channel><item> 요소
    fe = fg.add_entry()
    # <channel><item><title> 요소
    fe.title("파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발")
    # <channel><item><link> 요소
    fe.link(href="http://example.com")
    # <channel><item><description> 요소
    fe.description(
        '<a href="http://example.com">이스케이프 처리 확인 전용 링크</a>'
        "설명을 입력했다고 가정합니다.")
    # <channel><item><book:writer> 요소(사용자 정의 네임 스페이스를 사용하는 요소)
    fe.book.publisher({'name': "위키북스", 'id': "1"}) # 값은 딕셔너리 자료형으로 전달합니다.

    # 피드를 RSS 형식으로 변환(pretty=True로 들여쓰기 적용)
    return fg.rss_str(pretty=True)

if __name__ == '__main__':
    rss_str = create_feed()
    print(rss_str.decode())
