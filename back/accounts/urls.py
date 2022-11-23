from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    # 회원가입
    path("signup/", views.signup),
    # pk로 유저 정보 1개 가져와서 image 경로 얻기
    # 애초에 jwt 토큰 발급할때 원하는 유저정보를 더 포함시킬수도 있지만
    # 장고의 ImageField는 직렬화 불가능해서 이방법 사용..
    path("user/<int:pk>", views.getUser),
]
