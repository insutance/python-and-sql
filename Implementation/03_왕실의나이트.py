# 이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_115'

"""내가 작성한 코드"""
data = list(input())
x = ord(data[0])-96
y = int(data[1])

# L, R, U, D 순으로 움직일 수 있는 경우의 수 저장
move_types = [
    [-2, 0, -1, 0],
    [-2, 0, 0, 1],

    [0, 2, -1, 0],
    [0, 2, 0, 1],

    [-1, 0, -2, 0],
    [0, 1, -2, 0],

    [-1, 0, 0, 2],
    [0, 1, 0, 2]
]

count = 0
for move in move_types:
    # 0,1 인덱스는 수평 움직임 2,3 인덱스는 수직 움직임
    next_x = x + move[0] + move[1]
    next_y = y + move[2] + move[3]

    # 8x8 체스판을 넘어갔다면 count+1 안 하고 넘어가기
    if next_x < 1 or next_x > 8 or next_y < 1 or next_y > 8:
        continue
    
    # 8x8 체스판을 넘어가지 않았다면 count += 1
    count += 1

print(count)


""" 답안 예시 """
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (-1,2), (1,-2), (1,2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)