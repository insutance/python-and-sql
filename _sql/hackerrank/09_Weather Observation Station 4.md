## 📌 Problem
Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because `total number of records - number of unique city names = 3 - 2 =1`.

## 📌 Code
```sql
SELECT COUNT(CITY)-COUNT(DISTINCT(CITY))
FROM STATION;
```