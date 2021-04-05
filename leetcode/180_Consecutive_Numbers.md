## 📌 Problem
Link : https://leetcode.com/problems/consecutive-numbers/

<br>

## 📌 Code

```sql
select distinct ConsecutiveNums     -- distinct를 사용해 중복 값 제거
from (
    -- lead() 함수를 사용해 첫번째, 두번째 아래 row 값을 가져와 해당 row 값과 비교.
    -- 첫번째, 두번째 아래에 row 값과 num이 같다면 num 값을 추출
    -- 그렇지 않다면 null
    select if(num = lead(num,1) over(order by id) and num = lead(num,2) over(order by id)
              , num, null) as ConsecutiveNums
    from logs
)as tmp
where ConsecutiveNums is not null   -- null 값 제외
```