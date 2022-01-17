"""
Link: https://www.acmicpc.net/problem/1475

- collections 의 Counter 사용, 리스트에서 개수를 바로 딕셔너리 형태로 만들어 줌.
- Counter에서는 값이 존재하지 않아도 오류가 발생하지 않고, 0개를 출력해주기 때문에,
  6,9 개수를 출력할 수 있음.
- 두 수는 하나의 세트로 만들 수 있으니 (6개수 + 9개수 + 1) // 2 계산을 통해 몇 개의 세트가 필요한지 알아내 값을 동일하게 넣어줌.
- 딕셔너리 값 중에서 가장 큰 값을 출력하면 최소로 필요한 세트 수 추출.
"""

from collections import Counter

room_numbers = list(map(int, input()))
room_numbers = Counter(room_numbers)

room_numbers[6] = room_numbers[9] = (room_numbers[6] + room_numbers[9] + 1) // 2

print(max(room_numbers.values()))
