"""
Link: https://www.acmicpc.net/problem/1789

- 서로 다른 N개의 자연수의 합이 S
- 개수(N)가 최대값이 될 때를 찾아라.
- 1부터 쭉 더해주기
- for문에서 마지막 값은 -1 로 들어가기 때문에 +1 해주기
"""

s = int(input())

n = 0
sum_data = 0
for i in range(s + 1):
    sum_data += i
    if sum_data == s:
        print(i)
        break
    elif sum_data > s:
        print(i - 1)
        break
