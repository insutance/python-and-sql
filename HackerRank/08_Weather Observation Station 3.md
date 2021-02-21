## 📌 Problem
Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

The STATION table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

## 📌 Code
```sql
SELECT DISTINCT(CITY)
FROM STATION
WHERE ID%2=0
```