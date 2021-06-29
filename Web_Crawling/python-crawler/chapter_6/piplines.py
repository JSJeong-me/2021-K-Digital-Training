"""Quotes 아이템을 처리하는 파이프라인"""
from hashlib import sha256
from orator import DatabaseManager, Model
from orator.orm import belongs_to_many

from my_project.settings import ORATOR_CONFIG

db = DatabaseManager(ORATOR_CONFIG)
Model.set_connection_resolver(db)

class Quote(Model):
    """quotes 테이블 모델"""

    @belongs_to_many
    def tags(self):
        return Tag

class Tag(Model):
    """tags 테이블 모델"""
    
    @belongs_to_many
    def quote(self):
        return Quote

class DatabasePipeline(object):
    """MySQL에 Quotes 저장하기"""

    def __init__(self):
        """스크레이핑한 모든 item을 저장할 변수 선언"""
        self.items = []

    def process_item(self, item, spider):
        """각각의 아이템에 대한 처리"""
        self.items.append(item)
        return item

    def close_spider(self, spider):
        """spider 종류 후의 처리"""
        for item in self.items:
            text_hash = sha256(
                item['text'].encode('utf8', 'ignore')).hexdigest()
            exist_quote = Quote.where('text_hash', text_hash).get()

            if exist_quote:
                continue
            quote = Quote()
            quote.author = item['author']
            quote.text = item['text']
            quote.text_hash = text_hash
            quote.save()

            tags = []
            for tag_name in item['tags']:
                tag = Tag.where('name', tag_name).first()
                if not tag:
                    tag = Tag()
                    tag.name = tag_name
                    tag.save()
                tags.append(tag)
                quote_tags = quote.tags()
                quote_tags.save(tag)
