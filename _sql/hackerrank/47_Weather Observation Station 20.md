## 📌 Problem
A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from **STATION** and round your answer to `4` decimal places.

**Input Format**

The **STATION** table is described as follows:

![STATION TABLE](image/2021-02-21-20-10-15.png)

where LAT_N is the northern latitude and LONG_W is the western longitude.

<br>

## 📌 Code
```sql
set @row_id = 0;
set @cnt = (select count(*) from station);

select round(avg(LAT_N), 4)
from (
    select *
    from station
    order by LAT_N
)as tmp
where (select @row_id := @row_id + 1) between @cnt/2 and @cnt/2 + 1
```

`row_id`를 생성, station의 총 개수 `cnt` 생성
```sql
set @row_id = 0;
set @cnt = (select count(*) from station);
```

station 테이블을 `LAT_N` 을 기준으로 정렬한다.
```sql
select *
    from station
    order by LAT_N
```

`row_id`를 계속해서 `+1`해주면서 그 값이 `총 개수(cnt)/2` or `총 개수(cnt)/2+1` 사이 값이라면 이라는 where 절을 만든다.
```sql
where (select @row_id := @row_id + 1) between @cnt/2 and @cnt/2 + 1
```

### 다른 사람 코드
아래 코드는 홀수일 때는 될 것 같지만 짝수라면 불가능 할 것 같다.
```sql
select round(avg(LAT_N), 4)
from station as s
where (select count(*) from station where LAT_N < s.LAT_N) = (select count(*) from station where LAT_N > s.LAT_N)
```