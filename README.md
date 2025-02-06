# capstone

## 시스템 순서 요약
1. CSV 파일 업로드
2. 컬럼별 역할 선택
    - 식별자: 특정 개인을 식별할 수 있는 데이터 -> 삭제
    - 준식별자: 결합 등을 통해 개인을 식별할 수 있는 데이터 -> 가명처리
    - 민감정보: 정보주체의 사생활을 현저히 침해할 우려가 있는 개인정보 -> 가명처리 + 프라이버시 모델 적용
    - 비민감정보: 가명정보 처리 과정에서 영향이 없는 데이터 -> 가명처리 or 삭제
3. 준식별자, 민감정보로 선택된 컬럼에 대하여 적용할 가명처리 선택(단일)
4. 레벨별로 가명처리 진행
5. 프라이버시 모델을 적용하여 처리 가능한 조합 선택
6. 가명처리된 데이터 반환

## 가명처리 기법 설명
* 일반삭제: 컬럼 자체를 삭제
**Before**
     name  age    city
0   Alice   25   Seoul
1     Bob   30   Busan
2  Charlie   35  Incheon
3    David   40   Daegu
**After (컬럼 "age"와 "city" 삭제)**
     name
0   Alice
1     Bob
2  Charlie
3    David

* 부분삭제: 컬럼의 특정 인덱스 데이터의 일부를 삭제
**Before**
     name    age    city
0   Alice   12345   Seoul
1     Bob   67890   Busan
2  Charlie  54321  Incheon
3    David  98765   Daegu
**After (컬럼 "age"에서 인덱스 1~2의 부분 삭제: 범위 [1, 3])**
     name    age    city
0   Alice   1***   Seoul
1     Bob   6***   Busan
2  Charlie  5***   Incheon
3    David  9***   Daegu

* 행 항목 삭제: 컬럼의 특정 행을 삭제
**Before**
     name    age    city
0   Alice   25   Seoul
1     Bob   30   Busan
2  Charlie   35  Incheon
3    David   40   Daegu
**After (인덱스 1과 3 삭제)**
     name    age    city
0   Alice   25   Seoul
2  Charlie   35  Incheon

* 로컬삭제: 컬럼의 특정 인덱스 값 삭제
**Before**
     name    age    city
0   Alice   25   Seoul
1     Bob   30   Busan
2  Charlie   35  Incheon
3    David   40   Daegu
**After (컬럼 "name"에서 인덱스 1과 3 삭제)**
     name    age    city
0   Alice   25   Seoul
1           30   Busan
2  Charlie   35  Incheon
3           40   Daegu

* 마스킹: 컬럼 데이터에 마스킹 적용
**Before**
     name      age      city
0   Alice   12345    Seoul
1     Bob   67890    Busan
2  Charlie  54321   Incheon
3    David  98765    Daegu
**After (컬럼 "age"에서 인덱스 1~3을 마스킹)**
     name      age      city
0   Alice   12345    Seoul
1     Bob   *****    Busan
2  Charlie  *****   Incheon
3    David  *****    Daegu

* 주소: 도/시 기준으로 주소를 좁힘
**Before**
     address
0   Seoul Gangnam
1   Busan Haeundae
2   Incheon Yeonsu
3   Daegu Dalseo
**After (도 단위까지 삭제 - mode=1)**
     address
0   Seoul
1   Busan
2   Incheon
3   Daegu




{
    "삭제기술": ["일반삭제", "부분삭제", "행 항목 삭제", "로컬삭제", "마스킹", "주소"],
    "통계도구": ["총계처리", "부분총계"],
    "범주화 기술": ["일반 라운딩", "랜덤 라운딩", "로컬 일반화", "문자데이터 범주화"]
}
