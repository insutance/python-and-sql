## 📌 Problem
Query a count of the number of cities in CITY having a Population larger than .

**Input Format**

The CITY table is described as follows: 

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
SELECT COUNT(1) -- =COUNT(*)
FROM city
WHERE population > 100000;
```