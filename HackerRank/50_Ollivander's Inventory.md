## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem

<br>

## 📌 Code
Hackerrank 에서 `row_number() over (partition by ~)` 를 저번에 사용했었는데 이번에는 계속해서 오류가 발생했다..
아래 코드를 작성하고 `MS SQL Server`로 실행시켜보니 정답이였다.
```sql
with tmp as (
    select id, age, coins_needed, power,
        row_number() over (partition by power, age order by coins_needed) as rownumber
    from wands
    join wands_property on wands.code = wands_property.code
    where is_evil = 0
)
select id, age, coins_needed, power
from tmp
where rownumber = 1
order by power desc, age desc
```

`row_number() over (partition by~)` 사용해 `power`와 `age`로 묶어준 후 `coins_needed`로 오름차순으로 해준다.
```sql
select id, age, coins_needed, power,
        row_number() over (partition by power, age order by coins_needed) as rownumber
from wands
join wands_property on wands.code = wands_property.code
where is_evil = 0
```

`with 테이블명 as`를 사용해 임시 테이블을 생성해준다.
```sql
with tmp as (
    select id, age, coins_needed, power,
        row_number() over (partition by power, age order by coins_needed) as rownumber
    from wands
    join wands_property on wands.code = wands_property.code
    where is_evil = 0
)
```

`tmp` 테이블을 사용해 원하는 값을 뽑아내는데, `where rownumber=1`이면 power와 age가 같은 값들에서 가장 작은 `coins_needed`를 뽑아낸다는 뜻이다.
```sql
with tmp as (
    select id, age, coins_needed, power,
        row_number() over (partition by power, age order by coins_needed) as rownumber
    from wands
    join wands_property on wands.code = wands_property.code
    where is_evil = 0
)
select id, age, coins_needed, power
from tmp
where rownumber = 1
order by power desc, age desc
```