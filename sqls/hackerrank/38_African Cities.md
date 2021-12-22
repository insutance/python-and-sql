## 📌 Problem
Given the **CITY** and **COUNTRY** tables, query the names of all cities where the CONTINENT is 'Africa'.

**Note**: CITY.CountryCode and COUNTRY.Code are matching key columns.

**Input Format**

The **CITY** and **COUNTRY** tables are described as follows: 

![](image/2021-03-08-17-47-11.png)
![](image/2021-03-08-17-47-26.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

<br>

## 📌 Code
```sql
select city.name
from city
join country
on city.countrycode = country.code
where continent = 'Africa'
```