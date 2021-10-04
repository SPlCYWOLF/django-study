## 시험 준비

- schema, column

- ORM : sql 문 몰라도 파이썬에서 클래스를 통한 객체조작만으로 DB조작 가능하게 해주는 것. 장고 orm이 우리 대신에 쿼리문을 날려주니까 가능한거임.

  우리는 장고를 활용하여 DB를 클래스를 통한 인스턴스 생성을 통해 조작 가능하다.

- class Article() 은 DB에 article_articles 이름으로 저장된다

- makemigrations 을 통해 설계도를 만들고, migrate 로 해당 설계도를 DB에 반영해야한다.

- 어떤 필드를 추가하는데, 필드가 없으면 null인데, 거기에 어떤 벨류를 넣을거냐 하는 메세지를 받는다(?) 필드값 설정해라(?)

- showmigrations: migration이 DB에 됬는지 여부 확인

  sqlmigrate: 생성된 migrations파일들이 어떤 sql 문장을 실행하는지 보여줌

- DB API 구문 : Article.objects.all()

  .get()은 객체 반환 .all() 쿼리셋 반환

- ORM 문을 SQL문으로 쓰는 연습 ㄱ

<br>

- DB로 얻는 장점들

  데이터 중복 최소화, 데이터 무결성(정확한 정보를 보장), 데이터 일관성, 데이터 독립성(물리적 / 논리적), 데이터 표준화, 데이터 보안 유지

- 관계형 데이터베이스 (RDB)

  테이블에 형대로 열: 속성, 가로줄(행): 하나의 데이터

- 스키마를 기준으로 테이블들을 생성

- RDMBS 가 뭐냐

- SQL : 데이터베이스에 일을 시키기 위한 언어

- SQL 분류: 

  DDL-테이블 스키마 정의위함, CREATE DROP ALTER, 

  DML- INSERT, SELECT(조회), DELETE(특정 레코드 삭제)

  ​	ORDER BY, DISTINCT, FROM, LIMIT, OFFSET(리미트랑 같이다님), WHERE, 

  DCL- 

- 테이블 생성 및 삭제 연습해라

- sqlite에서 사용하는 `.` 은 sql 언어이다!

- autoincrement 뭐시기: pk 값 과 같이, 중복 사용 자동 방지

- sqlite aggregate functions

  COUNT, AVG, MAX, SUM, etc

  전체 가져오려면 `*` GHKFDYD

- LIKE operator

  특정한 패턴 매칭을 시키고싶으면 이거 활용.

  `%` == 있을수도, 없을수도있다

  `_` == 반드시 있다

- ORDER BY 컬럼 ASC

  ORDER BY 컬럼 DECS

- GROUP BY : 그룹핑해서 가져올때

  aggregate 머시기를 같이 활용

  AS 활용하면 Count 해당하는 컬럼에 별명을 줄 수 도 잇다

- ALTER TABLE : 테이블 변경!

<br>

- 대소관계 비교 조건 

  ```sqlite
  __gte, __lte, __gt, __lt
  ```

- filter() 는 & (and)만 사용 가능.

  고로, | (or) 쓰고싶으면 Q() 써야한다

- SQL 문은 항상 FROM 부터 읽는다

- 대소문자 구분 기준 

<br>

- .aggregate() 

  avg 나 sum 등 활용해서 집계하는 함수

- .annotate()

  집계한 데이터들을 임의적인 컬럼에 추가된 형태로 반환

  