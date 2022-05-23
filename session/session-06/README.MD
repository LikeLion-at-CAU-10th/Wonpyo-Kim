### 백엔드

1. [설명](#1설명)

![2022-05-22 (1)](https://user-images.githubusercontent.com/69501435/169689828-2f381823-c003-488c-8b3d-736f57c3a81b.png)

# 1.설명

## 1-1. 가상환경
- 서버내부의 깔려있는 프로그램들의 버전은 유지되어야 한다. 만약 외부에서 업데이트를 하게 되면 서버에 영향을 주게된다. 그러므로 서버의 버전관리를 위해 가상환경을 만들어 그걸 바탕으로 작업한다.
- 가상환경을 위한 virtualenv를 설치해야하며, 가상환경 내부에는 django프레임워크등 필요한 파일들을 다운받는다.

## 1-2. 프로젝트 및 앱 생성
- django-admin startproject [프로젝트이름] 으로 생성하자.
- 그후 [프로젝트이름]으로 파고들어가 manage.py를 찾자. 그 후 django-admin startapp [앱이름]을 만든다.

## 1-3. 기본 설정
- 프로젝트의 urls.py를 목표한 views.py나 다른 앱들의 urls과 연결시킨다.
- 기본적으로 app들마다 관리하고 있는 models.py가 있다. 그 부분들을 정의해주자
- 정의 후 순서는 항상 python manage.py makemigrations -> python manage.py migrate
## 2. what to do next
- 그 후 짜잘한 logic 들은 mtv모델을 이용하도록 한다. 
- views.py에서 model.py로부터 받은 모델들을 데이터 가공하여 template으로 혹은 바로 json파일로 전송할 수 있도록 한다.
