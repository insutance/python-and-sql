"""
https://www.acmicpc.net/problem/11723

- 구현하는 것은 쉽다. 하지만 "시간 초과"를 내지 않는 것이 중요한 문제였다.
- sys를 통해 값을 입력 받지 않으면 시간 초과 발생.

- discard() 라는 것을 처음으로 알게 됨.
- remove는 값이 존재하지 않으면 오류가 발생하기 때문에 값 체크 해야 하지만 discard는 값 체크가 필요없음.
"""

import sys

m = int(input())

result_set = set()
all_datas = set([i for i in range(1, 21)])

for _ in range(m):
    datas = sys.stdin.readline().strip().split()
    operation = datas[0]

    if len(datas) == 2:
        num = int(datas[1])
        if operation == "add":
            result_set.add(num)
        elif operation == "remove" and num in result_set:
            result_set.remove(num)
        elif operation == "toggle":
            if num in result_set:
                result_set.remove(num)
            else:
                result_set.add(num)
        elif operation == "check":
            if num in result_set:
                print(1)
            else:
                print(0)
    else:
        if operation == "all":
            result_set = all_datas
        elif operation == "empty":
            result_set = set()
            # result_set.clear() 이렇게 작성해도 됨.

"""
discard() 사용
"""
import sys

m = int(input())

result_set = set()
all_datas = set([i for i in range(1, 21)])

for _ in range(m):
    datas = sys.stdin.readline().strip().split()
    operation = datas[0]

    if len(datas) == 2:
        num = int(datas[1])
        if operation == "add":
            result_set.add(num)
        elif operation == "remove":
            result_set.discard(num)
        elif operation == "toggle":
            if num in result_set:
                result_set.discard(num)
            else:
                result_set.add(num)
        else:
            if num in result_set:
                print(1)
            else:
                print(0)
    else:
        if operation == "all":
            result_set = all_datas
        elif operation == "empty":
            result_set = set()
