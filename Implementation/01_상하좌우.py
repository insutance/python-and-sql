# 이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_111'

# 문제유형 : 시뮬레이션
# 시간복잡도 : O(N)
# 요구사항대로 구현하면 연산 횟수는 이동 횟수에 비례하기 된다.

"""내가 작성한 코드"""
n = int(input())
moves = input().split()

# 처음 시작 좌표 [x,y]
start = [1,1]

for move in moves:
    if move == 'U':
        if start[0]-1 > 1:
            start[0] -= 1

    elif move == 'D':
        if start[0]+1 < n:
            start[0] += 1

    elif move == 'L':
        if start[1]-1 > 1:
            start[1] -= 1

    elif move == 'R':
        if start[1]+1 < n:
            start[1] += 1

print(start)


"""답안 예시"""
n = int(input())
x,y = 1,1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x,y = nx, ny

print(x,y)