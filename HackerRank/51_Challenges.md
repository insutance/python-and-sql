## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/challenges/problem

<br>

## 📌 Code
```sql
with tmp1 as(
    select Hackers.hacker_id, Hackers.name, count(challenge_id) as challenges_created
    from Hackers
    join Challenges on Hackers.hacker_id = Challenges.hacker_id
    group by Hackers.hacker_id, Hackers.name
)

select *
from tmp1
where challenges_created = (select max(challenges_created) from tmp1) 
or challenges_created in (select challenges_created 
                          from tmp1 
                          group by challenges_created 
                          having count(challenges_created) = 1)
order by challenges_created desc, hacker_id
```

### 1. `with`을 사용해 `hacker_id`, `name`, `challenges_created` 을 가지는 임시 테이블 생성
```sql
with tmp1 as(
    select Hackers.hacker_id, Hackers.name, count(challenge_id) as challenges_created
    from Hackers
    join Challenges on Hackers.hacker_id = Challenges.hacker_id
    group by Hackers.hacker_id, Hackers.name
)
```

### 2. `challenges_created` 값이 maximum 값이라면 다 뽑아내야 함.
```sql
where challenges_created = (select max(challenges_created) from tmp1)
```

### 3. `count(challenges_created)` 값이 1인 값들만 뽑아내기
```sql
challenges_created in (select challenges_created 
                        from tmp1 
                        group by challenges_created 
                        having count(challenges_created) = 1)
```
위와 같이 하게 되면 `count(challenges_created) = 1` 인 값들만 select 된다. `in`을 사용해 `challenges_created`값이 `select`된 값들 안에 존재한다면 출력한다.

### 4. 완성된 where문
```sql
where challenges_created = (select max(challenges_created) from tmp1) 
or challenges_created in (select challenges_created 
                          from tmp1 
                          group by challenges_created 
                          having count(challenges_created) = 1)
```

### 5. 정렬
### 6. 완성된 코드
```sql
with tmp1 as(
    select Hackers.hacker_id, Hackers.name, count(challenge_id) as challenges_created
    from Hackers
    join Challenges on Hackers.hacker_id = Challenges.hacker_id
    group by Hackers.hacker_id, Hackers.name
)

select *
from tmp1
where challenges_created = (select max(challenges_created) from tmp1) 
or challenges_created in (select challenges_created 
                          from tmp1 
                          group by challenges_created 
                          having count(challenges_created) = 1)
order by challenges_created desc, hacker_id
```