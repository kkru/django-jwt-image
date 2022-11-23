from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):

    # image 필드 설정
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = get_user_model()
        fields = ("username", "image")
