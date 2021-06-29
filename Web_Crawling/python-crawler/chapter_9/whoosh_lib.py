import os

from whoosh import index
from whoosh.fields import Schema, ID, TEXT, NGRAM

# 인덱스 데이터를 저장할 디렉터리 지정하기
INDEX_DIR = "indexdir"

# 인덱스 전용 스키마 정의하기
schema = Schema(
    # 인덱스 유닛 ID로 글의 URL 사용하기
    post_url=ID(unique=True, stored=True),
    # 본문을 N그램으로 인덱스화
    body=NGRAM(stored=True),
)

def get_or_create_index():
    # 인덱스 전용 디렉터리가 없다면 만들기
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        # 인덱스 전용 파일 만들기
        ix = index.create_in(INDEX_DIR, schema)
        return ix
        
    # 이미 인덱스 전용 디렉터리가 있는 경우
    # 기존의 인덱스 파일 열어서 사용하기
    ix = index.open_dir(INDEX_DIR)
    return ix
