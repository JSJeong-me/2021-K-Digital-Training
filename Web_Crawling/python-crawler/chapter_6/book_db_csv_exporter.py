"""DB의 내용을 다양한 형식으로 출력하기"""
import csv
import io

####### 여기가 이전 코드의 ➊ 부분입니다.
import logging

from orator import DatabaseManager, Model
from orator.orm import belongs_to, has_many

# Orator가 어떤 SQL을 실행하는지 로그로 출력해서 확인하기
logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)

# MySQL 접속 설정
config = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'book_db',
        'user': 'root',
        'password': '',
        'prefix': '',
        'log_queries': True,
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)

# 각 테이블과 객체의 관계성 정의
# 클래스 이름이 소문자 또는 스네이크 케이스로 변경돼 테이블의 이름과 대응됨
class Language(Model):
    """언어의 종류"""
    pass

class Book(Model):
    """도서"""
    # books 테이블의 language_id에 해당하는 데이터 가져오기
    @belongs_to
    def language(self):
        """책의 언어"""
        return Language
    # publishers 테이블의 publisher_id에 해당하는 데이터 가져오기
    @belongs_to
    def publisher(self):
        """책의 출판사"""
        return Publisher

class Publisher(Model):
    """출판사"""
    # 하나의 출판사에는 여러 도서가 들어갈 수 있음
    @has_many
    def books(self):
        """출판사의 도서들"""
        return Book
####### 종료

# 변환 함수
def create_csv():
    """CVS 만들기"""
    output = io.StringIO()
    csv_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    header = ["id", "title", "url", "publisher_id", "publisher_name", "language_id", "language_name"]
    csv_writer.writerow(header)
    publisher = Publisher.all()
    publisher.load('books', 'books.language')  # Eager Loading
    for publisher in publisher:
        for book in publisher.books:
            line = [
                book.id,
                book.title,
                book.publisher.id,
                book.publisher.name,
                book.language.id,
                book.language.name,
            ]
            csv_writer.writerow(line)
        return output.getvalue()

# main 실행 블록
if __name__ == '__main__':
    csv_str = create_csv()
    print(csv_str)
