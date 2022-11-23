# 이미지 처리

1. 장고에 media 경로 설정 처리
   1. 프로젝트 경로에 media 폴더 생성
   2. settings.py 에 media 경로 설정 추가
   3. urls.py 에 static 경로 설정
2. ImageField사용 (이미지가 필요한 모델 , 시리얼라이저에 추가)
3. 프론트에서 ```<input type="file">``` 태그 사용해서 파일 업로드(자세한건 vue 파일 참조)
   1. 파일을 담아서 요청을 보낼때는 json으로 처리 힘들기 때문에 form data로 전송
   2. 헤더에 인코딩을위해 데이터에 파일 포함되어 있다고 설정해주기
4. 이후 이미지 필요한 경우 저장 경로 불러와서 장고 서버 주소 뒤에 이미지 경로 붙여서 요청 (ex: "http//127.0.0.1:8000/media/image.jpg")
