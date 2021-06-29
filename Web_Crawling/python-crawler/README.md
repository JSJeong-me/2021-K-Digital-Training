책의 예제 파일과 관련된 추가 설명 파일입니다.

# 6장 

## 프로젝트 파일의 일부
프로젝트를 만드는 경우, 프로젝트 파일 전체를 예제 파일로 넣는 것은 찾아보는 것을 오히려 힘들게 만들 수 있을 것이라 생각해서, 필요한 파일만 넣었습니다. 복사해서 사용해주세요.

- 코드 6-13 items.py = chapter_6/items.py
- 코드 6-14 quotes.py = chapter_6/quotes_1.py
- 코드 6-15 quotes.py = chapter_6/quotes_2.py
- 코드 6-18 quotes.py = chapter_6/quotes_3.py
- 코드 6-22 quotes.py = chapter_6/quotes_4.py
- 코드 6-24 piplines.py = chapter_6/piplines.py

## 설정 변화에 의해 바뀔 수 있는 코드
코드 6-26, 코드 6-27과 같은 설정 파일은 Scrapy 버전 변화에 따라서 바뀌는 경우가 굉장히 많습니다. 프로젝트를 생성한 후, 책에 적혀있는 것들만 추가해주세요. 복사해서 사용할 수 있게 첨부해보았습니다.

```python
ITEM_PIPELINES = {
    'my_project.pipelines.DatabasePipeline': 300,
}
```
```python
DEPTH_LIMIT = 1
ORATOR_CONFIG = {
    'mysql': {
        'driver': 'mysql',
        'host': 'localhost',
        'database': 'quotes',
        'user': 'root',
        'password': '',
        'prefix': '',
        'log_queries': True,
    }
}
```


# 7장

## 프로젝트 파일의 일부

- 코드 7-15 models.py = chapter_7/models.py
- 코드 7-17 views.py = chapter_7/views.py
- 코드 7-18 urls.py = chapter_7/urls.py

## 설정 변화에 의해 바뀔 수 있는 코드
코드 7-16와 같은 설정 파일은 Django 버전 변화에 따라서 바뀌는 경우가 굉장히 많습니다. 프로젝트를 생성한 후, 책에 적혀있는 것들만 추가해주세요. 조금 긴 부분은 ➐의 다음 부분인데, 이는 복사해서 사용할 수 있게 첨부해보았습니다.

```python
REST_FRAMEWORK = { 
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'PAGE_SIZE': 10
}
```

# 8장

## 프로젝트 파일의 일부

- 코드 8-8 models.py = chapter_8/models.py
- 코드 8-10 admin.py = chapter_8/admin.py

