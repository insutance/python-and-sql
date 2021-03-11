## 📌 Problem
Consider `P1(a,c)` and `P2(b,d)` to be two points on a 2D plane where `(a,b)` are the respective minimum and maximum values of Northern Latitude (LAT_N) and `(c,d)` are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

Query the Euclidean Distance between points `P1` and `P2` and format your answer to display 4 decimal digits.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
-- pow(x,y) : x의 y제곱근 값을 반환
-- sqrt(x)  : 양수 x 에 대한 제곱근을 반환

select round(sqrt(pow((max(LAT_N)-min(LAT_N)),2) + pow((max(LONG_W)-min(LONG_W)),2)),4)
from station
```