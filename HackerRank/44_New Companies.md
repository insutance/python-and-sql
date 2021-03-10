## 📌 Problem

Link : https://www.hackerrank.com/challenges/the-company/problem

<br>

## 📌 Code
```sql
select company_code, founder,
        (select count(distinct lead_manager_code) from lead_manager l where c.company_code = l.company_code),
        (select count(distinct senior_manager_code) from senior_manager s where c.company_code = s.company_code),
        (select count(distinct manager_code) from manager m where c.company_code = m.company_code),
        (select count(distinct employee_code) from employee e where c.company_code = e.company_code)
from company c
order by company_code
```
```sql
-- result
C1 Angela 1 2 5 13 
C10 Earl 1 1 2 3 
C100 Aaron 1 2 4 10 
C11 Robert 1 1 1 1 
C12 Amy 1 2 6 14 
C13 Pamela 1 2 5 14 
C14 Maria 1 1 3 5 
C15 Joe 1 1 2 3 
C16 Linda 1 1 3 5 
C17 Melissa 1 2 3 7 
C18 Carol 1 2 5 6 
C19 Paula 1 2 4 7 
C2 Frank 1 1 1 3 
C20 Marilyn 1 1 2 2 
C21 Jennifer 1 1 3 7 
C22 Harry 1 1 3 6 
C23 David 1 1 1 2 
C24 Julia 1 1 2 6 
C25 Kevin 1 1 2 5 
C26 Paul 1 1 1 3 
{-truncated-}
```