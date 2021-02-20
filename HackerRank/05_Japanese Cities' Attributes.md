## 📌 Problem
Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:

![](image/2021-02-20-14-40-11.png)

## 📌 Code
```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE='JPN';
```