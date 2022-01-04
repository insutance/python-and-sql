"""
Link: https://www.acmicpc.net/problem/2217

- 거꾸로 정렬을 한 후, (index+1) 값과 곱함으로써 병렬로 연결했을 때의 최대 중량을 구한다.
- 모든 값을 배열에 저장한 후, 가장 큰 값을 뽑아낸다.
"""

n = int(input())
ropes = []
for _ in range(n):
    rope = int(input())
    ropes.append(rope)

ropes.sort(reverse=True)

max_weights = [ropes[i] * (i + 1)for i in range(len(ropes))]
print(max(max_weights))
