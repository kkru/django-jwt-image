from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# 회원가입 처리
@api_view(["POST"])
def signup(request):
    password = request.data.get("password")
    password_confirm = request.data.get("passwordConfirm")

    if password != password_confirm:
        return Response(
            {"error : 비밀번호가 일치하지 않습니다!"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = UserSerializer(data=request.data)

    print(request.data)

    # 데이터 유효성 검증
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()

        # 암호화
        user.set_password(request.data.get("password"))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 사용자 정보 1개 리턴
@api_view(["GET"])
def getUser(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    print(user)
    serializer = UserSerializer(user)
    return Response(serializer.data)
