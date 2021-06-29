"""API 전용 뷰"""
from rest_framework import serializers, viewsets

# film/models.py 읽어 들이기
from film import models

# models.py의 Language 모델 데이터를 JSON으로 변환하는 클래스
class LanguageSerializer(serializers.ModelSerializer):
    """Language 시리얼라이저"""
    class Meta:
        model = models.Language  # models.Language와 연결
        fields = '__all__'  # 모든 필드 출력하기

# models.py의 Film 모델 데이터를 JSON으로 변환하는 클래스
class FilmSerializer(serializers.ModelSerializer):
    """Film 시리얼라이저"""
    # language 필드에는 위의 LanguageSerializer 적용하기
    language = LanguageSerializer()
      
    class Meta:
        model = models.Film  # models.Film과 연결
        fields = '__all__'  # 모든 필드 출력하기

# /films의 URL에서 호출될 클래스
class FilmViewSet(viewsets.ModelViewSet):
    """Film 전용 ViewSet"""
    # Film 모델에서 쿼리 객체를 추출하고, queryset에 설정(필수)
    queryset = models.Film.objects.all()

    # 직렬화 해당 지정(필수)
    serializer_class = FilmSerializer

    # 옵션
    filter_fields = '__all__'
    ordering_fields = '__all__'
    search_fields = ('title',)
