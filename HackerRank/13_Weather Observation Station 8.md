## 📌 Problem
Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

</br>

## 📌 Code
```sql
SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY,1) IN ('a','e','i','o','u') 
      and RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u');
```

## 📌 Others Code
```sql
SELECT City
FROM Station
WHERE City REGEXP '^[aeiou]' and City REGEXP '[aeiou]$';

-- ^a : a로 시작하는 패턴
-- a$ : a로 끝나는 패턴

-- ^[aeiou] : 대괄호([]) 안에 있는 내용들로 시작하는 패턴
-- [aeiou]$ : 대괄호([]) 안에 있는 내용들로 끝나는 패턴
```

## 📌 정규식 공부링크
👉 [MySQL REGEXP](https://codingdog.tistory.com/entry/mysql-regexp-%EB%B3%B5%EC%9E%A1%ED%95%9C-%ED%8C%A8%ED%84%B4-%EB%A7%A4%EC%B9%AD%EC%9D%84-%ED%95%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4)