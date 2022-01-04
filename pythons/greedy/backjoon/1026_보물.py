"""
Link: https://www.acmicpc.net/problem/1026

- 가장 작은 값과 가장 큰 값을 곱해주면 되는 문제.
- 단 첫번째로 받은 배열은 정렬해도 되지만 두번째로 받은 배열은 정렬해서는 안 됨.

- a_datas.sort()를 통해 작은 순서대로 정렬.
- pop(), index(), max()를 사용해 b_datas 배열에서 큰 값들만 뽑아오기.
- 작은 순서대로 정렬된 a_datas와 b_datas에서 가장 큰 값을 뽑아와 곱한 후 sum에 저장.
"""

n = int(input())
a_datas = list(map(int, input().split()))
b_datas = list(map(int, input().split()))

a_datas.sort()

sum = 0
for i in range(n):
    max_value = b_datas.pop(b_datas.index(max(b_datas)))
    sum += a_datas[i] * max_value
    
print(sum) 