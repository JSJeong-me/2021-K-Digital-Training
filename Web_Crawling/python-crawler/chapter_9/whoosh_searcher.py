import sys
from whoosh_lib import get_or_create_index
from whoosh.qparser import QueryParser

if __name__ == '__main__':
    # 인덱스 읽어 들이기
    ix = get_or_create_index()

    # 키워드 입력 프롬프트를 출력해서, 키워드 입력받기
    keyword = input("검색 키워드를 입력해주세요: ") 

    # body 필드를 대상으로 문자열 검색
    with ix.searcher() as searcher: 
        # 키워드를 사용해서 검색 쿼리 객체 만들기
        query = QueryParser("body", ix.schema).parse(keyword)
        # 검색 실행
        results = searcher.search(query)
        if not results:
            print('검색 결과가 없습니다.')
            sys.exit(0)
        print('검색 결과를 출력합니다.')
        for i, r in enumerate(results):
            print("{}: post_url: {}".format(i + 1, r['post_url']))