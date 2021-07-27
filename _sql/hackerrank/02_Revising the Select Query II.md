## 📌 Problem
Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.

The CITY table is described as follows:

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
SELECT NAME
FROM CITY
WHERE POPULATION >= 120000 and COUNTRYCODE='USA';
```