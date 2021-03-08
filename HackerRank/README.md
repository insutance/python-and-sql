## 📁 SQL
- [올림, 반올림, 내림 - ceil(), round(), floor()](#ceil-round-floor)
- [문자열 길이 가져오기 - length() vs char_length()](#length-charlength)
- [문자열 자르기 - left(), substring(), right()](#left-substring-right)
- [문자열 더하기 - concat()](#concat)
- [문자열 변경하기 - replace()](#replace)
- [문자열 반복 - repeat()](#repeat)
- [유니온 - union](#union)
- [사용자 정의 변수 - set](#set)

<br>

<h3 name="ceil-round-floor">📌 올림, 반올림, 내림</h3>

1. 올림 `ceil()`
```sql
CEIL(1.9) => 2
CEIL(1.1) => 2
```

2. 반올림 `round()`
```sql
SELECT round(1.9)   => 2
SELECT round(1.1)   => 1
```

3. 내림 `floor()`
```sql
SELECT floor(1.9)  => 1
SELECT floor(1.1)  => 1
```

</br>

<h3 name="length-charlength">
📌 문자열 길이 가져오기 `LENGTH()` vs `CHAR_LENGTH()`</h3>

- `LENGTH()` : Byte 길이를 가져옴 **(한글은 정확히 길이를 알 수 없음)**
- `CHAR_LENGTH()` : Byte 수를 계산하지 않고 단순히 몇 개의 문자가 있는지 가져옴

</br>

<h3 name="left-substring-right">
📌 문자열 자르기 (left, substring, right)</h3>

```
Schema : test
Talbe : actor

|  name  | 
+--------+
| 유재석 |
```
1. 왼쪽에서 문자열 자르기 </br>
**`left(칼럼명 or 문자열, 자를 길이)`**</br>
```sql
SELECT LEFT(name,1)
FROM test.actor
-- result : 유

SELECT LEFT(name,2)
FROM test.actor
-- result : 유재

SELECT LEFT(name,3)
FROM test.actor
-- result : 유재석
```
2. 중간에서 문자열 자르기 <br>
**`SUBSTRING(칼럼명 or 문자열, 시작위치, 길이)`**</br>
```sql
SELECT SUBSTRING(name, 2, 1)
FROM test.actor
-- result : 재

SELECT SUBSTRING(name, 1, 2)
FROM test.actor
-- result : 유재

SELECT SUBSTRING(name, 3, 1)
FROM test.actor
-- result : 석
```
3. 오른쪽에서 문자열 자르기 <br>
**`RIGHT(칼럼명 or 문자열, 자를 길이)`**</br>
```sql
SELECT RIGHT(name, 1)
FROM test.actor
-- result : 석

SELECT RIGHT(name, 2)
FROM test.actor
-- result : 재석

SELECT RIGHT(name, 3)
FROM test.actor
-- result : 유재석
```
4. 구분자(Delimiter) delim가 count만큼 나오기 전에 str에서 서브 스트링 리턴<br>
**`SUBSTRING_INDEX(str, delim, count)`**<br>
```sql
SELECT SUBSTRING_INDEX(name, '석', 1)
FROM test.actor
-- result : 유재
-- '석'이라는 문자가 1번 나오기 전에 서브 스트링 리턴

SELECT SUBSTRING_INDEX(name, '석', 2)
FROM test.actor
-- result : 유재석
-- '석'이라는 문자가 2번 나오기 전에 서브 스트링 리턴
-- 여기서는 '유재석' 이기 때문에 '석'이 1번 나왔으므로 모두 출력
```

</br>

<h3 name="concat">📌 문자열 더하기 - concat()</h3>

`CONCAT()` : 문자열 이어주는 역할

- 조건1 : `name`으로 정렬, `occupation`의 첫번째 단어를 괄호로 묶어서 출력.<br>
- 조건2 : `occpuation`을 `GROUP BY`를 통해 묶은 후 `COUNT()`로 갯수 출력,<br> `LOWER()`를 통해 `occupation`을 소문자로 출력<br>
`COUNT(occupation)`(=그룹한 개수로 정렬) 후 `occupation`(=알파벳 순서)로 정렬.

</br>

<h3 name="replace">📌 문자 변경하기 - replace()</h3>

`replace(칼럼명, '변경하려고 하는 문자', '변경할 문자')`<br>
```
Schema : test
Talbe : actor

|  name  | salary |
+--------+--------|
| 유재석 |  7025  |
```
```sql
select replace(name, '재', '자')
from test.actor;
-- result : 유자석
```
`replace()`는 문자 타입만 가능한 줄 알았다. 하지만 아니었다.<br>
`salary`의 타입이 `integer`이지만 `replace()`를 사용해 0을 제거할 수 있었다.
```sql
select replace(salary, 0, '')
from test.actor;
-- result : 725
```

</br>

<h3 name="repeat">📌 문자열 반복 - repeat()</h3>

형식 : `repeat(str, count)`<br>
`str`은 반복할 문자이고 `count`는 반복되는 횟수이다.
```sql
set @number := 5; 

select repeat('* ', @number := @number-1)
from information_schema.tables
limit 5;
```
```sql
--result

* * * * * 
* * * * 
* * * 
* * 
*
```

</br>

<h3 name="union">📌 union</h3>

`union`은 여러개의 SQL문을 합쳐 하나의 SQL문으로 만들어주는 방법이다.<br>
(= 두개의 쿼리의 합집합을 만들어준다.)

- `union` : 두 쿼리의 결과의 중복값을 제거해서 보여줌
- `union all` : 중복되는 값도 전부 다 보여줌

<`union` 규칙>
- 칼럼명이 같아야 한다. (같지 않다면 `AS`를 사용하여 같게 만든다.)
- 칼럼별 데이터타입이 같아야 한다.

</br>

<h3 name="set">📌 사용자 정의 변수 - set</h3>

```sql
-- 사용자 정의 변수 선언 및 초기화

set @변수이름 = 대입값;
set @변수이름 := 대입값;

select @변수이름 := 대입값; -- 출력까지 할 때.
```
대입 연산자 `:=` <br>
set 이외의 명령문에서는 `=`가 비교연산자로 취급되기 때문에 SELECT로 변수를 선언하고 값을 대입할 때는 `:=`를 사용한다.

저장하는 값에 의해 자료형이 정해지며, `Integer`, `Decimal`, `Float`, `Binary` 그리고 `String` 타입만 취급할 수 있다. 또한 변수를 초기화 하지 않은 경우 값은 `NULL`, 자료형은 `String` 타입이다.