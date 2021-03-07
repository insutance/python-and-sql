## 📌 Problem
Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than `137.2345`. Truncate your answer to 4 decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
select round(max(LAT_N), 4)
from station
where LAT_N < 137.2345
```