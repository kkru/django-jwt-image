from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 이미지 필드 사용
    # upload_to : 파일 업로드 경로 ( media 경로 내 )
    # default : DB 기본값
    image = models.ImageField(upload_to="%Y/%m/%d", default="")
