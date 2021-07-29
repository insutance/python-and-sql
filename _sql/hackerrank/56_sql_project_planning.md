## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/sql-projects/problem

<br>

## 📌 Code

```sql
SELECT start_date, MIN(end_date)
FROM 
    (SELECT start_date FROM projects WHERE start_date NOT IN (SELECT end_date FROM projects)) a,
    (SELECT end_date FROM projects WHERE end_date NOT IN (SELECT start_date FROM projects)) b
where start_date < end_date
GROUP BY start_date
ORDER BY datediff(start_date, MIN(end_date)) DESC, start_date
```

**<풀이>**
- 다른 프로젝트의 종료 날짜가 아닌 시작 날짜를 선택<br>(시작 날짜가 종료 날짜인 경우 동일한 프로젝트의 일부임)
- 다른 프로젝트의 종료일이 아닌 종료일을 선택
- where절에서 시작 날짜와 종료 날짜가 반드시 일치하지 않아도 되는 목록이 있어야 함.
- 이렇게 하면 시작 날짜 이후의 종료 날짜만 선택하고 특정 start_date에 대해 MIN을 선택하면 다른 작업의 시작과 일치하지 않는 가장 가까운 종료 날짜를 얻는다.