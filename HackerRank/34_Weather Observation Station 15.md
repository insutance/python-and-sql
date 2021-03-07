## 📌 Problem
Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than `137.2345`. Round your answer to 4 decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
-- LAT_N을 기준으로 내림차순으로 정렬
-- 맨 위에 값만 뽑아내면 LAT_N의 최대값
-- LAT_N이 최대값인 row의 LOGN_W를 출력

select round(LONG_W, 4)
from station
where LAT_N < 137.2345
order by LAT_N desc
limit 1;
```

```sql
-- where 절에서 max(LAT_N) 값을 찾아내는 쿼리문

select round(LONG_W, 4)
from station
where LAT_N = (
    select max(LAT_N)
    from station
    where LAT_N < 137.2345
)
```