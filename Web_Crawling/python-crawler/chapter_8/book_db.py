"""데이터베이스 모델"""
import datetime

import peewee
from playhouse.pool import PooledMySQLDatabase

db = PooledMySQLDatabase(
    'book_db',
    max_connections=8,
    stale_timeout=10,
    user='root')

class BaseModel(peewee.Model):
    """공통 부모 모델"""

    created_at = peewee.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = peewee.DateTimeField()

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow()
        super().save(*args, **kwargs)

    class Meta:
        database = db

class Publisher(BaseModel):
    id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField()
    is_active = peewee.BooleanField()

    class Meta:
        db_table = 'publisher'
