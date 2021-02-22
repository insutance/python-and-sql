## 📌 Problem
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Sample Input**

For example, CITY has four entries: DEF, ABC, PQRS and WXY.

**Sample Output**
```
ABC 3
PQRS 4
```

**Explanation**

When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths 3,3,4 and 3. The longest name is PQRS, but there are 3 options for shortest named city. Choose ABC, because it comes first alphabetically.

**Note**

You can write two separate queries to get the desired output. It need not be a single query.

</br>

## 📌 Code
```sql
SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY 2, 1
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM STATION
ORDER BY 2 DESC, 1 DESC
LIMIT 1;
```

## 📌 Others Code
```sql
(SELECT CITY, LENGTH(CITY) 
 FROM STATION 
 ORDER BY 2,1 
 LIMIT 1)
UNION
(SELECT CITY, LENGTH(CITY) 
 FROM STATION 
 ORDER BY 2 DESC, 1 DESC 
 LIMIT 1)
```

## 📌 Study

**1. 문자열 길이 가져오기 `LENGTH()` vs `CHAR_LENGTH()`**
- `LENGTH()` : Byte 길이를 가져옴 **(한글은 정확히 길이를 알 수 없음)**
- `CHAR_LENGTH()` : Byte 수를 계산하지 않고 단순히 몇 개의 문자가 있는지 가져옴

</br>

**2. union**</br>
`union`은 여러개의 SQL문을 합쳐 하나의 SQL문으로 만들어주는 방법이다.<br>
(= 두개의 쿼리의 합집합을 만들어준다.)

- `union` : 두 쿼리의 결과의 중복값을 제거해서 보여줌
- `union all` : 중복되는 값도 전부 다 보여줌

<`union` 규칙>
- 칼럼명이 같아야 한다. (같지 않다면 `AS`를 사용하여 같게 만든다.)
- 칼럼별 데이터타입이 같아야 한다.
