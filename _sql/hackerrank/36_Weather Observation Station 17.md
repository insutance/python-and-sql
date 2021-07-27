## 📌 Problem
Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than `38.7780`. Round your answer to 4 decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
select round(LONG_W, 4)
from station
where LAT_N = (
    select min(LAT_N)
    from station
    where LAT_N > 38.7780
)
```