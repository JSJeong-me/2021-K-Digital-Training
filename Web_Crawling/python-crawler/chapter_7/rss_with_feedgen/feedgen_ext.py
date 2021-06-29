"""feedgen 확장 네임 스페이스(book: http://my-service.com/xmlns/book)."""
from lxml import etree
from feedgen.ext.base import BaseExtension

class BookBaseExtension(BaseExtension):
    """book 확장 네임 스페이스"""

    # 사용자 정의 네임 스페이스의 URL
    BOOK_NS = "http://my-service.com/xmlns/book"

    def __init__(self):
        """사용자 정의 요소 이름 앞에는 __를 넣습니다."""
        # 변수는 딕셔너리 자료형으로 넣습니다.
        self.__publisher = {}

    def extend_ns(self):
        """확장 네임 스페이스"""
        return {'book': self.BOOK_NS}

    def _extend_xml(self, elm):
        """요소 추가하기"""
        if self.__publisher:
            publisher = etree.SubElement(
                elm, # 부모 요소
                '{%s}publisher' % self.BOOK_NS, # {<네임 스페이스의 URL>}요소 이름
                attrib={'id': self.__publisher.get('id')} # id 속성 적용
            )
            publisher.text = self.__publisher.get('name') # 요소의 내용 적용
        return elm

    def publisher(self, name_and_id_dict=None):
        """self.__publisher"""
        if name_and_id_dict is not None:
            name = name_and_id_dict.get('name')
            id_ = name_and_id_dict.get('id')
            if name and id_:
                self.__publisher = {'name': name, 'id': id_}
            elif not name and not id_: # name이 없는 경우는 요소를 만들지 않음
                self.__publisher = {}
            else:
                raise ValueError('name과 id를 함께 지정해주세요.')
        return self.__publisher

class BookFeedExtension(BookBaseExtension):
    """channel 요소에 적용"""

    def extend_rss(self, rss_feed):
        """요소 추가 때 호출"""
        channel = rss_feed[0]
        self._extend_xml(channel)

class BookEntryExtension(BookBaseExtension):
    """item 요소에 적용"""
    
    def extend_rss(self, entry):
        """요소 추가 때 호출"""
        self._extend_xml(entry)
