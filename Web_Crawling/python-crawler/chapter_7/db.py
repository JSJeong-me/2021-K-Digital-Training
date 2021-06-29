"""데이터베이스 모델"""
import peewee
from playhouse.pool import PooledMySQLDatabase

# sakila 데이터베이스에 접근하기 위한 정보
db = PooledMySQLDatabase(
    'sakila',
    max_connections=8,
    stale_timeout=10,
    user='root')

class BaseModel(peewee.Model):
    """기본 부모 모델"""
    class Meta:
        database = db

class Language(BaseModel):
    """language 테이블 전용 모델"""

    language_id = peewee.SmallIntegerField(primary_key=True)
    name = peewee.CharField(max_length=20)
    last_update = peewee.TimestampField()

    class Meta:
        db_table = 'language'

class Film(BaseModel):
    """film 테이블 전용 모델"""
    
    film_id = peewee.SmallIntegerField(primary_key=True)
    title = peewee.CharField(index=True)
    description = peewee.TextField(null=True)
    release_year = peewee.DateField(formats="%Y")
    # 외부키
    language = peewee.ForeignKeyField(Language)
    length = peewee.SmallIntegerField()
    last_update = peewee.TimestampField()
    def to_dict(self):
        return {
            'film_id': self.film_id,
            'title': self.title,
            'description': self.description,
            'release_year': self.release_year,
            'language': self.language.name,
            'length': self.length,
            'last_update': self.last_update.isoformat(),
        }

    class Meta:
        db_table = 'film'
