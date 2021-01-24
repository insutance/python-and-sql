def solution(n):
    # 값이 들어갈 삼각형을 이중배열로 생성
    triangle = [[0 for j in range(i)] for i in range(1,n+1)]
    
    num = 1
    x,y = 0,0
    direction = "down"                      # 첫 방향은 아래로 움직임

    for i in range(n):                  
        if direction == "down":             # 방향이 아래일 때는 x값을 1씩 더해주면서 값을 넣는다.
            for j in range(i, n):
                triangle[x][y] = num
                x += 1                      
                num += 1                    
            x -= 1                          # x를 -1, y를 +1 해줌으로써 좌표를 설정    
            y += 1
            direction = "right"             # 아래로 움직인 후에는 오른쪽으로 이동
        
        elif direction == "right":          # 방향이 오른쪽일 때는 y값을 1씩 더해주면서 값을 넣는다.
            for j in range(i, n):
                triangle[x][y] = num
                y += 1
                num += 1
            x -= 1                          # x를 -1, y를 -2 해줌으로써 좌표를 설정
            y -= 2
            direction = "up"                # 오른쪽으로 움직인 후에는 대각선으로 이동
        
        elif direction == "up":             # 방향이 위로올라갈때는(대각선) x, y값을 1씩 빼면서 값을 넣는다.
            for j in range(i, n):
                triangle[x][y] = num
                x -= 1
                y -= 1
                num += 1
            x += 2                          # x를 +2, y를 +1 해줌으로써 좌표를 설정
            y += 1
            direction = "down"              # 대각선이동 후 아래쪽으로 이동
    
    answer = []
    for i in range(len(triangle)):          # triangle 이중배열을 더해주면서 하나의 배열로 생성
        answer += triangle[i]

    return answer
        
"""
훨씬 간단한 코드
"""
def solution2(n):
    triangle = [[0 for j in range(i)] for i in range(1,n+1)]
    
    num = 1
    x,y = -1,0

    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                x += 1
            elif i%3 == 1:
                y += 1
            elif i%3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    
    answer = []
    for i in range(len(triangle)):
        answer += triangle[i]
    
    return answer
        
print(solution(4))

"""
triangle[0][0] = 1
triangle[1][0] = 2
triangle[2][0] = 3
triangle[3][0] = 4
triangle[4][0] = 5
triangle[5][0] = 6
triangle[6][0] = 7

triangle[6][1] = 8
triangle[6][2] = 9
triangle[6][3] = 10
triangle[6][4] = 11
triangle[6][5] = 12
triangle[6][6] = 13

triangle[5][5] = 14
triangle[4][4] = 15
triangle[3][3] = 16
triangle[2][2] = 17
triangle[1][1] = 18

------------------------------
triangle[2][1] = 19
triangle[3][1] = 20
triangle[4][1] = 21
triangle[5][1] = 22

triangle[5][2] = 23
triangle[5][3] = 24
triangle[5][4] = 25

triangle[4][3] = 26
triangle[3][2] = 27

-----------------------------
triangle[4][2] = 28
"""