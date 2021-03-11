## 📌 Problem
Consider `P1(a,b)` and `P2(c,d)` to be two points on a 2D plane.

 `a` happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 `b` happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 `c` happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 `d` happens to equal the maximum value in Western Longitude (LONG_W in STATION).
Query the Manhattan Distance between points `P1(a,b)` and `P2(c,d)` and round it to a scale of 4 decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
-- abs() 절대값을 구하는 함수

select round(abs(min(LAT_N)-max(LAT_N)) + abs(min(LONG_W)-max(LONG_W)), 4)
from station
```