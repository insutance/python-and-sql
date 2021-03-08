## 📌 Problem
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
```
* 
* * 
* * * 
* * * * 
* * * * *
```
Write a query to print the pattern P(20).

<br>

## 📌 Code
```sql
set @number = 0; 

select repeat('* ', @number := @number+1)
from information_schema.tables
limit 20;
```

```sql
set @number = 0; 
select repeat('* ', @number := @number+1)
FROM information_schema.tables
WHERE @number < 20;
```