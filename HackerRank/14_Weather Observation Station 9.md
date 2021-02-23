## 📌 Problem
Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

</br>

## 📌 Code
```sql
-- 정규식 사용하기
-- ^[^...] : 대괄호([]) 안에 있는 내용들(...)로 시작하지 않는 문자열
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[^aeiou]'


-- LEFT(), NOT IN 사용하기
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) NOT IN ('a','e','i','o','u');
```