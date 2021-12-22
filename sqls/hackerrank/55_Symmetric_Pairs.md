## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/symmetric-pairs/problem

<br>

## 📌 Code

```sql
select f1.x, f1.y
from functions f1
join functions f2
on f1.x = f2.y and f1.y = f2.x
group by f1.x, f1.y
having count(*) > 1 or f1.x < f1.y
order by f1.x
```
**<주의할 점>**

1. X = Y 인 경우 같은 데이터가 하나 더 있어야지 짝꿍으로 쳐준다. 
sample input에서 첫째줄과 둘째줄에 20,20이 있는데, 만약 한줄만 있었으면 짝꿍이 없는것!

2. X <= Y 인 케이스만 적어주면 된다. 
sample input 에서 3번째줄, 6번째줄이 짝꿍인데 X <= Y 인 20, 21을 출력해주고 21,20은 출력해주지 않는다.

**<풀이>**
- functions 테이블을 self join
- 중복 제거를 위해 group by 사용
- having 절에서 count가 1보다 큰 쌍만 필터링 해준다. <br>
주의할 점 1번을 통해 x=y 이지만, 쌍이 한개인 컬럼은 여기서 필터링 되어서 포함되지 않는다.
- 주의할 점 2번을 통해 `f1.x < f1.y` 를 having 절에서 필터링 해준다.