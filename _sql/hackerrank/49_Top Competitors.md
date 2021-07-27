## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/full-score/problem

<br>

## 📌 Code
```sql
--최종코드

select h.hacker_id, h.name
from Submissions as s
join Hackers as h on s.hacker_id = h.hacker_id
join Challenges as c on s.challenge_id = c.challenge_id
join Difficulty as d on c.difficulty_level = d.difficulty_level
where s.score = d.score
group by 1,2
having count(h.hacker_id) > 1
order by count(h.hacker_id) desc, h.hacker_id
```

### 1. submissions table을 base로 필요한 정보를 담고 있는 테이블들을 join 해야함.
  1) hacker의 이름을 출력하기 위해 Hackers 테이블이 필요.
  2) difficulty level 정보가 있어야 full score 를 연결할 수 있고, 그 정보는 Challenges 테이블에 있음.
  3) 제출한 문제의 full score 를 알기 위해 difficuly 테이블의 score 정보가 필요.

```sql
from Submissions as s
join Hackers as h on s.hacker_id = h.hacker_id
join Challenges as c on s.challenge_id = c.challenge_id
join Difficulty as d on c.difficulty_level = d.difficulty_level
```

### 2. full score 인 컬럼만 뽑기
```sql
where s.score = d.score
```

### 3. hacker_id 별 full score 맞은 문제 갯수 count 하고, 2개 이상 푼 사람만 추출
`group by`로 `hacker_id`, `name` 으로 묶어준 뒤, 개수가 1이상 인 칼럼만 뽑아준다 `count(h.hacker_id) > 1`.
```sql
group by s.hacker_id, h.name
having count(h.hacker_id) > 1
```

### 4. 개수가 많은 순으로 내림차순으로 정렬, hacker_id로 오름차순 정렬
```sql
order by count(h.hacker_id) desc, h.hacker_id
```

### 추가설명
having 절, order by 절에서 굳이 `count(h.hacker_id)`를 해줄 필요가 없다. `count(h.name)`해도 결국 같은 값이 나오고 `count(*)`해도 같은 값이 나온다. `group by`로 묶은 후 계산을 하는 것이기 때문에 모두 같은 값이 나올 것이다.