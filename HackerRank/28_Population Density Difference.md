## 📌 Problem
Query the difference between the maximum and minimum populations in CITY.

**Input Format**

The CITY table is described as follows: 

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
select max(population) - min(population)
from city
```