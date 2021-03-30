## 📌 Problem
문제링크 : https://www.hackerrank.com/challenges/contest-leaderboard/problem
<br>

## 📌 Code
1. 문제 이해하기
submissions 테이블을 보면 한 명의 해커가 같은 문제를 여러번 풀었을 때 각 점수가 다르다. 그 중에서 큰 값을 가져와야 한다.
2. Sub Query를 사용해 여러번 풀었다면 그 중 큰 값을 가져오는 submissions 테이블 생성하기
3. 그 후 hackers와 join
4. 총 점수(sum(score))가 0이면 제외 시키기 때문에 `having`절 사용
5. 점수별로는 내림차순, 이름별로 오름차순으로 정렬

```sql
select h.hacker_id, name, sum(score)
from (
    select hacker_id, challenge_id, max(score) score
    from Submissions 
    group by 1,2
) as s
join hackers h on s.hacker_id = h.hacker_id
group by 1,2
having sum(score) > 0
order by 3 desc, 1
```