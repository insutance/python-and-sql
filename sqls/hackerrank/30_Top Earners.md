## 📌 Problem
![](image/2021-03-06-00-03-23.png)
![](image/2021-03-06-00-03-44.png)
![](image/2021-03-06-00-04-04.png)

## 📌 Code
```sql
select months * salary, count(months * salary)
from employee
where (months * salary) = (
    select max(months * salary)
    from employee
)
group by 1
```
