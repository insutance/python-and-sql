# 이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_119'

# 문제유형 : 시뮬레이션
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""

n,m = map(int, input().split())
x,y,d = map(int, input().split())

maps = []
for i in range(m):
    maps.append(list(map(int, input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 방문한 위치를 리스트 안에 튜플로 저장
visited = [(x,y)]

rotation_cnt = 0
while True:
    d = (d+3) % 4
    nx = x + dx[d]
    ny = y + dy[d]

    # 칸을 넘어가면 회전
    if nx < 0 or nx > m or ny < 0 or ny > m:
        continue
    
    # 회전한 후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if (nx,ny) not in visited and maps[ny][nx] == 0:
        x,y = nx,ny
        visited.append((x,y))
        rotation_cnt = 0
    # 회전한 후 정면에 가보지 않은 칸이 없거나 바디인 경우
    else:
        rotation_cnt += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if rotation_cnt == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        # 뒤로 갈 수 있다면 이동
        if maps[ny][nx] == 0:
            x,y = nx, ny
        # 뒤가 바다일 경우 break
        else:
            break
        rotation_cnt = 0

# 방문한 배열 길이 print
print(len(visited))


""" 답안 예시 """
n,m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 x,y 좌표 및 방향 입력
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북,동,남,서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x,y = nx,ny
        count += 1
        turn_time = 0
        continue
    # 회전한 후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x,y = nx,ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)