## 📌 Problem
Query the total population of all cities in CITY where District is California.

**Input Format**

The CITY table is described as follows: 

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
SELECT SUM(population)
FROM city
WHERE district = 'California';
```