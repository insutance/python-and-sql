"""
이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_97'
"""

"""
핵심내용
#1. 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는 것
"""

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)               # 현재 줄(입력받은 줄)에서 '가장 작은 수 찾기'
    result = max(result, min_value)     # '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)


"""
처음 내가 작성한 코드
"""
n, m = map(int, input().split())

result = 0
cards = []
for i in range(n):
    # 굳이 cards 배열을 만들고, 추가해줄 필요가 없음
    cards.append(list(map(int, input().split())))

    # 작은 값을 찾고 max()함수를 사용해 두 개의 숫자를 비교해버리면 됨.
    if i == 0:
        result = min(cards[i])
    elif result < min(cards[i]):
        result = min(cards[i])

print(result)