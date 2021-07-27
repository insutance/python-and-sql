## 📌 Problem
Link : https://leetcode.com/problems/department-highest-salary/

<br>

## 📌 Code
```sql
-- 방법1
with max_salary_of_department as(
    -- 각 부서의 최대 salary 값 추출한 테이블
    select departmentId, max(salary) max_salary
    from employee
    group by departmentId
)
select d.name Department, e.name Employee, e.salary Salary
from employee e
join department d on e.departmentId = d.id
join max_salary_of_department ms on e.departmentId = ms.departmentId
where e.salary = ms.max_salary      -- salary와 max_salary 값 비교
```

```sql
-- 방법2
with salary_rank_by_department as(
    -- rank() 함수 사용
    select name, salary, departmentId, rank() over(partition by departmentId order by salary desc) r
    from employee
)
select d.name Department, sr.name Employee, sr.salary Salary
from salary_rank_by_department sr
join department d on sr.departmentId = d.id
where r = 1     -- rank가 1인 것만 뽑도록 조건 설정
```