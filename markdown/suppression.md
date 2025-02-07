# 삭제기술
## 1. 일반삭제: 컬럼 자체를 삭제

**Before**
```
name      age    city
0   Alice   25   Seoul
1   Bob     30   Busan
2   Charlie 35   Incheon
3   David   40   Daegu
```

**After** (컬럼 "age"와 "city" 삭제)
```
name
0   Alice
1   Bob
2   Charlie
3   David
```

---

## 2. 부분삭제: 컬럼의 특정 인덱스 데이터의 일부를 삭제

**Before**
```
name     income      city
0   Alice   12345   Seoul
1   Bob     67890   Busan
2   Charlie 54321   Incheon
3   David   98765   Daegu
```

**After** (컬럼 "income" 부분 삭제: 범위 [1, 4])
```
name     income    city
0   Alice   1   Seoul
1   Bob     6   Busan
2   Charlie 5   Incheon
3   David   9   Daegu
```

---

## 3. 행 항목 삭제: 컬럼의 특정 행을 삭제

**Before**
```
name     age    city
0   Alice   25   Seoul
1   Bob     30   Busan
2   Charlie 35   Incheon
3   David   40   Daegu
```

**After** (인덱스 1과 3 삭제)
```
name     age    city
0   Alice   25   Seoul
2   Charlie 35   Incheon
```

---

## 4. 로컬삭제: 컬럼의 특정 인덱스 값 삭제

**Before**
```
name     age    city
0   Alice   25   Seoul
1   Bob     30   Busan
2   Charlie 35   Incheon
3   David   40   Daegu
```

**After** (컬럼 "name"에서 인덱스 1과 3 삭제)
```
name     age    city
0   Alice   25   Seoul
1           30   Busan
2   Charlie 35   Incheon
3           40   Daegu
```

---

## 5. 마스킹: 컬럼 데이터에 마스킹 적용

**Before**
```
name     income      city
0   Alice   12345   Seoul
1   Bob     67890   Busan
2   Charlie 54321   Incheon
3   David   98765   Daegu
```

**After** (컬럼 "income"에서 범위 1~3을 마스킹)
```
name     income    city
0   Alice   1***5   Seoul
1   Bob     6***0   Busan
2   Charlie 5***1   Incheon
3   David   9***5   Daegu
```

---

## 6. 주소: 도/시 기준으로 주소를 좁힘

**Before**
```
address
0   Seoul Gangnam
1   Busan Haeundae
2   Incheon Yeonsu
3   Daegu Dalseo
```

**After** (도 단위까지 삭제 - mode=1)
```
address
0   Seoul
1   Busan
2   Incheon
3   Daegu
```
