## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/placements/problem

<br>

## 📌 Code

```sql
with students_salary as(
    -- students별 salary
    select s.id, s.name, p.salary
    from students s
    join packages p on s.id = p.id
)
, friends_salary as(
    -- friends별 salary
    select f.id, f.friend_id, p.salary
    from friends f
    join packages p on f.friend_id = p.id
)
select ss.name
from students_salary ss
join friends_salary fs 
-- join 할 때, 'students의 salary'와 'friends의 salary'를 비교
on ss.id = fs.id and ss.salary < fs.salary
order by fs.salary
```