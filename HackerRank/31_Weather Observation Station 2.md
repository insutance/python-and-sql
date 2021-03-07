## 📌 Problem
Query the following two values from the STATION table:

1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

**Output Format**

Your results must be in the form:
```
lat lon
```
where `lat` is the sum of all values in LAT_N and `lon` is the sum of all values in LONG_W. Both results must be rounded to a scale of 2 decimal places.

## 📌 Code
```sql
-- 합계에서 2번째 소수점까지 나오도록 출력.
-- round() 사용.

select round(sum(LAT_N),2), round(sum(LONG_W),2)
from station;
```