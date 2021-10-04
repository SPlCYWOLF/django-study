

# MTV

[TOC]



## 내 위치 찾기

![image-20210831103831273](가상환경.assets/image-20210831103831273.png)

- 내 위치 찾기 : ls

- 폴더 속에 폴더로 들어가고 싶을 때는 : cd ..



## 가상환경

### 가상환경 만들기

![image-20210831100857589](가상환경.assets/image-20210831100857589.png)

- python -m venv venv

  

### 가상환경 켜기

![image-20210831100939353](가상환경.assets/image-20210831100939353.png)

- source venv/Scripts/activate



### 가상환경 끄기

![image-20210831100951841](가상환경.assets/image-20210831100951841.png)

- deactivate



### 터미널 깨끗히 청소

![image-20210831101233855](가상환경.assets/image-20210831101233855.png)

- 터미널 청소하는 법 : ctrl + l



### 가상환경 내 라이브러리 검색

![image-20210831101351011](가상환경.assets/image-20210831101351011.png)

- pip list



### 장고 설치하기

![image-20210831101543168](가상환경.assets/image-20210831101543168.png)

- pip install django

![image-20210831101629361](가상환경.assets/image-20210831101629361.png)

---> pip install django 하면 pip list 이렇게 변경됨

### 가상환경 내에 라이브러리를 저장해주는 방법(당장 중요하진 않음)

![image-20210831101711753](가상환경.assets/image-20210831101711753.png)

![image-20210831101741684](가상환경.assets/image-20210831101741684.png)

![image-20210831101848433](가상환경.assets/image-20210831101848433.png)

- requirements 내에 있는 라이브러리 전체 설정



### .gitignore 파일 만들기(VScode, windows, Django, (python, macOS))

![image-20210831102408235](가상환경.assets/image-20210831102408235.png)



## 장고(Django) 시작하기

> **장고 = 1개 프로젝트 + N개 어플리케이션**

### 프로젝트 만들기

![image-20210831173145510](가상환경.assets/image-20210831173145510.png)

- 어플리케이션 만드는 명령어

![image-20210831102537613](가상환경.assets/image-20210831102537613.png)

- 프로젝트 만드는 명령어



### 서버 실행하러 가보기

![image-20210831102637090](가상환경.assets/image-20210831102637090.png)

- python manage.py runsever

![image-20210831102719374](가상환경.assets/image-20210831102719374.png)

- 빨간색 밑에 http://127.0.0... 그걸 ctrl + 마우스 왼쪽 누르기

![image-20210831102759746](가상환경.assets/image-20210831102759746.png)

- 로켓이 떴다!

![image-20210831103013971](가상환경.assets/image-20210831103013971.png)

----> 이렇게 생겼니? check 부탁쓰



### __init__.py 절대 건들지 않기!

![image-20210831103044069](가상환경.assets/image-20210831103044069.png)

- 비어있지만 건들지 마쇼 제발

- 당장 건들 것 (settings.py, urls.py)
- ![image-20210831103257694](가상환경.assets/image-20210831103257694.png)

### settings.py

- 우리가 설정할 기본 골격이다



### urls.py



### manage.py

- 상호작용 하기 (?)

- 언젠가 만나게 될 것임 두근두근



## 어플리케이션 생성하기

![image-20210831103702947](가상환경.assets/image-20210831103702947.png)

- 하고 나면
- ![image-20210831103737692](가상환경.assets/image-20210831103737692.png)
- 이런게 생긴다 (articles 폴더)

### admin.py





### apps.py





### models.py

- Model을 관리하는 것





### tests.py

- 테스트를 하기 위한 코드를 짜는 곳



### views.py

- view 함수 정의





## 진짜 시 작!

### ★★★★ 출생신고 해주기

![image-20210831104801621](가상환경.assets/image-20210831104801621.png)



![image-20210831104814439](가상환경.assets/image-20210831104814439.png)

- articles -> 어플리케이션



### url 만들기

![image-20210831111342499](가상환경.assets/image-20210831111342499.png)

- urls.py 누르기

![image-20210831111600561](가상환경.assets/image-20210831111600561.png)

- from _어플리케이션_ import _views_

![image-20210831111631126](가상환경.assets/image-20210831111631126.png)

- urlpatterns 안에 path('index/',views.index)

- index에 / : 끝에 / 붙이는게 표준이라서..

- 빨간색 물음표 안에는 함수 이름을 적어줍니다!



#### 요기까지 해주고 중간 관리자(views)가 할 일 적어주기!

![image-20210831111645182](가상환경.assets/image-20210831111645182.png)

- 클래스 / **함수** 만들어서 사용 가능 (클래스는 함축시켜서 표현하기 때문에 이해하기 힘들다!!)

- 클래스는 나중에 함수부터 만들기
- ![image-20210831111759280](가상환경.assets/image-20210831111759280.png)

- ![image-20210831111835323](가상환경.assets/image-20210831111835323.png)

	#### 시험에 나오기 좋아요

- 장고는 가장 처음에 인자를 항상 **request**를 사용함 ★★★★★

![image-20210831112250793](가상환경.assets/image-20210831112250793.png)

- 새 폴더 생성 -> **templates** -> 무조건 !!!

![image-20210831112356456](가상환경.assets/image-20210831112356456.png)



- index.html 만들기

![image-20210831112425768](가상환경.assets/image-20210831112425768.png)

- **!+tap** 누르면 나오는 html 파일 자동 설정
- body에다가 내용을 적어줄 것임

![image-20210831112420869](가상환경.assets/image-20210831112420869.png)

- html 문서 내용 추가

![image-20210831112642852](가상환경.assets/image-20210831112642852.png)

- templates 폴더 잘 만들었으면 딱히 'templates/index.html' 이라고 적지 않아도 됨

![image-20210831112721278](가상환경.assets/image-20210831112721278.png)

- 이런 모양으로 만들면 된다.

### html 열어보기



![image-20210831112922972](가상환경.assets/image-20210831112922972.png)



![image-20210831112933671](가상환경.assets/image-20210831112933671.png)

- 주소에 index 치면 나온다 !!

### 언어 설정

![image-20210831113414357](가상환경.assets/image-20210831113414357.png)



![image-20210831113457390](가상환경.assets/image-20210831113457390.png)



![image-20210831113548213](가상환경.assets/image-20210831113548213.png)

![image-20210831113709213](가상환경.assets/image-20210831113709213.png)

- 시간 설정



### greeting 만들기

![image-20210831131648795](가상환경.assets/image-20210831131648795.png)

- greeting 함수 설정 해주기

![image-20210831131754085](가상환경.assets/image-20210831131754085.png)

- greeting.html 파일 만들기

![image-20210831132131068](가상환경.assets/image-20210831132131068.png)



![image-20210831132610584](가상환경.assets/image-20210831132610584.png)



![image-20210831132948713](가상환경.assets/image-20210831132948713.png)



![image-20210831132811630](가상환경.assets/image-20210831132811630.png)

![image-20210831132902674](가상환경.assets/image-20210831132902674.png)

- 장고 주석 : ctrl + /

![image-20210831132838084](가상환경.assets/image-20210831132838084.png)



![image-20210831133056470](가상환경.assets/image-20210831133056470.png)



![image-20210831133138613](가상환경.assets/image-20210831133138613.png)

![image-20210831202802805](가상환경.assets/image-20210831202802805.png)

- a 태그에 href 랑 form 태그에 action에 양쪽 슬래시(/) 적어야 함 !
- 매서드 get은 **사용자 데이터를 변경하지 않는** 요청..(form 태그)에서만 사용되어야 한다.



#### 실습

![image-20210831133533611](가상환경.assets/image-20210831133533611.png)

![image-20210831133612178](가상환경.assets/image-20210831133612178.png)

- 실습 따라해보기

![image-20210831142225214](가상환경.assets/image-20210831142225214.png)

- random : import써서 사용

![image-20210831142219530](가상환경.assets/image-20210831142219530.png)

![image-20210831142235016](가상환경.assets/image-20210831142235016.png)

- for문 쓰는거
- **endfor** 꼭 써주기

![image-20210831142903681](가상환경.assets/image-20210831142903681.png)

![image-20210831142852775](가상환경.assets/image-20210831142852775.png)

- for문, if문 등등 실습했다!

![image-20210831143254285](가상환경.assets/image-20210831143254285.png)

- 수업에서 다양한 fliter을 써보기 위한 예시



![image-20210831143916905](가상환경.assets/image-20210831143916905.png)



![image-20210831143942304](가상환경.assets/image-20210831143942304.png)

- for문 + if문

![image-20210831154049731](가상환경.assets/image-20210831154049731.png)

- 상속....(일껄?)

### 상속



#### URL 상속된 후의 모습

![image-20210831203721480](가상환경.assets/image-20210831203721480.png)

- 부모 클래스에서 부모 urls.py를 설정할 때 include를 사용해서 자식 urls.py로 요청을 라우팅 해준다.

![image-20210831203830156](가상환경.assets/image-20210831203830156.png)

- 자식 urls.py에 가지고 온 모습
- name='index' => 별명을 지어서 유지 관리하기 편하게끔 만들어 둠

#### name='index' 사용 방법

![image-20210831203944429](가상환경.assets/image-20210831203944429.png)

- 원래는

```django
<a href = "/index/">메인 페이지로 돌아가자!</a>
```

- 별명 사용하면

```django
<a href = "{% url 'index' %}">메인 페이지로 돌아가자!</a>
```



### 부트스트랩 상속시키기

#### 상속법

![image-20210831204318852](가상환경.assets/image-20210831204318852.png)

- 자식 탬플릿 사진

![image-20210831204408697](가상환경.assets/image-20210831204408697.png)

- 예시 : 부트스트랩의 NAV바를 이용한 사진.
- line 49~50에

```django
  {% block content %}
  {% endblock %}
```

- 이걸 쓰면 자식 탬플릿에서 여기 중간에 글이 들어감

- block content를 꼭 쓰지 않아도 됨(ex. header, footer, div .....)



### 페이지 error 메세지

- 4로 시작하면 client 문제이고, 5로 시작하면 server 문제

