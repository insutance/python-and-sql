## 📌 Problem
Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.

The CITY table is described as follows:

![CITY table](image/2021-02-19-22-55-48.png)

## 📌 Code
```sql
SELECT *
FROM CITY
WHERE COUNTRYCODE = 'USA' and POPULATION >= 100000;
```
