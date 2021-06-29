"""URL 라우팅 정의 """
from django.conf.urls import url, include
from rest_framework import routers         
from film import views           
router = routers.DefaultRouter()   

# /films의 URL에 views.FilmViewSet 연결하기
router.register(r'films', views.FilmViewSet) 

urlpatterns = [
    url(r'^', include(router.urls)), 
]