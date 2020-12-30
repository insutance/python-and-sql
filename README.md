# Coding Test
프로그래머스에 있는 코딩테스트 문제를 풀어보쟈:)
<br/><br/>

## enumerate( )
- 반복문 사용시 몇 번째 반복문인지 확인이 필요할 때 사용
- 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환

ex)
```python
t = [1,5,7,33,39,52]
for p in enumerate(t):
    print(p)
```
```python
# result
(0,1)
(1,5)
(2,7)
(4,39)
(5,52)
```
<br/>

## collections.Counter( )
- 리스트의 원소들의 개수를 알고 싶을 때 사용한다.
- 인스턴스 간 더하기, 빼기, 교집합, 합집합 등의 기능도 추가로 이용할 수 있다.
- `Counter()`를 사용하기 위해선 `collections` 를 import 해야한다.
- `collections.Counter()` 의 결과값은 딕셔너리 형태이다.
```python
#Lv1.완주하지 못한 선수 문제를 아래와 같이 풀 수 있음
import collections

def solution2(participant, completion):
    #참가자와 완주자 수를 구한 후 빼면 => 완주하지 못한 선수
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```
<br/>

## list.sort( ) 와 sorted(list) 차이점
- `sort()` 함수는 **원본 리스트를 변경**하는 것이고, **반환값은 None**이다.
- `sorted()` 함수는 **원본 리스트를 변경하는 것은 아니다.** <br/>
반환값으로는 **새로운 배열을 만들어낸다.**

<br/>

## // 연산자
- 몫을 구할 때 '//' 연산자를 통해 몫만 가져올 수 있다.

<br/>

## sum( )
- `sum()`함수는 리스트에 있는 것들을 더해주는 함수이다.
- 이때 인자로는 iterable한 자료형을 받으며 **numeric** 해야한다. <br>
즉 리스트나 튜플처럼 **인덱스 순환 접근이 가능한 자료형**이고, **숫자로만** 이루어져 있어야 한다.

<br/>

## upper( ), lower( ), isupper( ), islower( )
- 대문자를 소문자로, 소문자를 대문자로 변경할 때 `upper()`, `lower()`를 사용할 수 있다.
```python
'a'.upper() # result : A
'A'.lower() # result : a
```
- `isupper()`, `islower()`를 통해 대문자인지 소문자인지 판별할 수 있다.<br>
반환형은 **Bool 타입**이다.
```python
'a'.isupper()   # result : False
'a'.islower()   # result : True
```

<br>

## join( ) 과 split( )
- `join()` 을 사용해 **"리스트->문자열"** 로 만들어줄 수 있다.
- `join()` 앞에 **''.join()** 이 붙는데, 이 안에 **':'.join()** 이렇게 콜론을 넣게되면<br>
    리스트의 각각이 문자열로 더해질 때 사이사이에 ':' 이 붙게 된다.
    **'/'.join()**을 하게되면 g/f/e/d/c/b/Z 이런식으로 결과가 나오게 된다.
- `split()` 은 **"문자열->리스트"** 로 만들어줄 수 있다.<br>
    string.split( ) **or** string.split('/') 후자는 '/'를 기준으로 나누는 것을 의미한다.<br>
    기본은 공백을 기준으로 나누는 것을 의미한다.

<br>

## isnumeric( ), isalpha( ), isdigit( )
- `isnumeric()` 을 사용해 숫자인지 판별함
- `isalpha()` : 문자열이 영어로 되어있는지 판별(한글도 영어로 취급함)
- `isdigit()` : 문자열이 숫자인지 판별 (numeric()함수보다는 더 작은 부분..?)

<br>

- isdigit( )은 제곱이나 세제곱 표현 된 특수기호까지 인정을 해준다.
- isnumeric( )은 제곱근 및 분수, 거듭제곱 특수문자까지 모두 인정을 해준다.
- isnumeric > isdigit 느낌

<br>

- `isdecimal()` 도 있지만 isdigit()보다 작은 느낌이라 사용하지 않으려고 함. 

<br>

## '에라토스테네스의 체' 알고르즘
- 주로 소수를 구할때 사용하는 알고리즘
- 범위에서 합성수를 지우는 방식으로 소수를 찾는 방법이다.
- 쉽게 생각하면, **배수를 지우는 방식**으로 소수를 찾는 것이다.

<br>

## zip( )
- `zip()`은 **'동일한 개수'**로 이루어진 자료형을 묶어주는 역할을하는 함수
```python
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]

>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
```

<br>

## reverse( )
- 리스트의 요소를 뒤집을 때 사용한다.
```python
list = [0,10,20,30]
list.reverse()
 
print(list)     # [30, 20, 10, 0]
```

<br>

## 최대공약수, 최소공배수
- `math` 모듈에 있는 `gcd`함수를 사용해서 쉽게 구할 수 있다.
- **최대공약수(Greatest Common Divisor)** : 두 수의 약수들 중 최대값
- **최소공배수(Least Common Multiple)** : 두 수의 곱에서 두 수의 최대공약수를 나눈 것과 같다.
```python
from math import gcd

_gcd = gcd(3, 12)           # 최대공약수
_lcm = (3 * 12) // _gcd     # 최소공배수

print(_gcd, _lcm)           # result : 3 12
```

<br>

## abs( )
- 절대값을 반환해주는 함수
```python
abs(-3)      # result : 3
abs(12)      # result : 12
```