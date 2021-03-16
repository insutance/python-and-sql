## 📌 Problem
![](2021-03-16-23-23-14.png)
![](2021-03-16-23-24-05.png)
![](2021-03-16-23-24-21.png)

<br>

## 📌 Code
```sql
select if(g.grade > 7, s.name, NULL), g.grade, s.marks
from students as s
join grades as g
on s.marks >= g.min_mark and s.marks <= g.max_mark
-- on s.marks between g.min_mark and g.max_mark
order by 2 desc, 1
```