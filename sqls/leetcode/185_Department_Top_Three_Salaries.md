## 📌 Problem
Link : https://leetcode.com/problems/department-top-three-salaries/

<br>

## 📌 Code
```sql
with top_three_salaries as(
    -- dense_rank() 함수 사용
    select name, salary, departmentId, dense_rank() over(partition by departmentId order by salary desc) dr
    from employee
)
select d.name Department, tts.name Employee, tts.salary Salary
from top_three_salaries tts
join department d on tts.departmentId = d.id
where dr < 4    -- rank가 4 미만인 값들만 추출하기 위해 조건 설정
```