## 📌 Problem
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

</br>

## 📌 Code
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
```

## 📌 Others Code
```sql
-- 정규식 사용
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY REGEXP '^[aeiou]';
```

```sql
select distinct CITY 
from STATION 
where CITY RLIKE '^[AEIOU]'
```

```sql
SELECT City
FROM Station
WHERE City LIKE 'A%' or City LIKE 'E%' or City LIKE 'I%' or City LIKE 'O%' or City LIKE 'U%';
```

```sql
-- 맨 처음 작성한 코드 (MySQL은 원하는 결과 안 나옴)
-- MS SQL Server에서는 가능
SELECT CITY 
FROM STATION 
WHERE CITY LIKE '[aeiou]%';
```

## 📌 Study

### 문자열 자르기
```
Schema : test
Talbe : actor

|  name  | 
+--------+
| 유재석 |
```
1. 왼쪽에서 문자열 자르기 </br>
**`left(칼럼명 or 문자열, 자를 길이)`**</br>
```sql
SELECT LEFT(name,1)
FROM test.actor
-- result : 유

SELECT LEFT(name,2)
FROM test.actor
-- result : 유재

SELECT LEFT(name,3)
FROM test.actor
-- result : 유재석
```
2. 중간에서 문자열 자르기 <br>
**`SUBSTRING(칼럼명 or 문자열, 시작위치, 길이)`**</br>
```sql
SELECT SUBSTRING(name, 2, 1)
FROM test.actor
-- result : 재

SELECT SUBSTRING(name, 1, 2)
FROM test.actor
-- result : 유재

SELECT SUBSTRING(name, 3, 1)
FROM test.actor
-- result : 석
```
3. 오른쪽에서 문자열 자르기 <br>
**`RIGHT(칼럼명 or 문자열, 자를 길이)`**</br>
```sql
SELECT RIGHT(name, 1)
FROM test.actor
-- result : 석

SELECT RIGHT(name, 2)
FROM test.actor
-- result : 재석

SELECT RIGHT(name, 3)
FROM test.actor
-- result : 유재석
```
4. 구분자(Delimiter) delim가 count만큼 나오기 전에 str에서 서브 스트링 리턴<br>
**`SUBSTRING_INDEX(str, delim, count)`**<br>
```sql
SELECT SUBSTRING_INDEX(name, '석', 1)
FROM test.actor
-- result : 유재
-- '석'이라는 문자가 1번 나오기 전에 서브 스트링 리턴

SELECT SUBSTRING_INDEX(name, '석', 2)
FROM test.actor
-- result : 유재석
-- '석'이라는 문자가 2번 나오기 전에 서브 스트링 리턴
-- 여기서는 '유재석' 이기 때문에 '석'이 1번 나왔으므로 모두 출력
```