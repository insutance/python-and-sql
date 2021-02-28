## 📌 Problem
Query the average population for all cities in CITY, rounded down to the nearest integer.

**Input Format**

The CITY table is described as follows: 

![CITY table](image/2021-02-20-14-36-14.png)

## 📌 Code
```sql
SELECT ROUND(AVG(population))
FROM city;
```

## 📌 Study (올림, 반올림, 내림)

### 1. 올림 `ceil()`
```sql
CEIL(1.9) => 2
CEIL(1.1) => 2
```

### 2. 반올림 `round()`
```sql
SELECT round(1.9)   => 2
SELECT round(1.1)   => 1
```

### 3. 내림 `floor()`
```sql
SELECT floor(1.9)  => 1
SELECT floor(1.1)  => 1
```