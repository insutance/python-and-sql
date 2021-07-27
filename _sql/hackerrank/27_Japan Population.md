## 📌 Problem
Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.

**Input Format**

The CITY table is described as follows: 

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
SELECT SUM(population)
FROM city
WHERE countrycode = 'JPN';
```