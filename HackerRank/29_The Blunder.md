## 📌 Problem
![](image/2021-03-03-21-39-30.png)
![](image/2021-03-03-21-39-54.png)

## 📌 Code
```sql
select ceil(avg(salary) - avg(replace(salary, 0, '')))
from employees;
```

## 📌 Study
`replace(칼럼명, '변경하려고 하는 문자', '변경할 문자')`<br>
`replace()`는 문자 타입만 가능한 줄 알았다.<br>
`salary`의 타입이 `integer`이지만 `replace()`를 사용해 0을 제거할 수 있었다.