def solution(board, moves):
    box = []    # stack 빈 배열 생성
    count = 0   # return 값 0 초기화
    for move in moves:                          # moves를 돌면서 하나씩 가져와 반복문 실행
        for i in range(len(board)):             # board의 index를 가져와 반복문 실행
            if board[i][move-1] == 0:           # 해당 값이 0 이면 빈 공간
                continue                        # continue를 통해 다음 반복문 실행
            else:
                box.append(board[i][move-1])    # 해당 값을 stack(box) 에 추가
                board[i][move-1] = 0            # borad값은 0으로 바꿔줌
                break                           # 0이 아닌 값을 찾으면 반복문 중단
        
        if len(box) >= 2:                       # box의 길이가 2이상이면 삭제될 것이 있으므로 길이 체크
            if box[-1] == box[-2]:              # stack(box) 마지막것과 두번째 마지막 값이 같다면
                box = box[:-2]                  # 두개를 삭제한 나머지 배열을 box에 대입
                count += 2                      # 삭제된 개수 +2
    
    return count


def solution2(board, moves):
    box = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:           # 위의 코드에서 더 간단하게
                box.append(board[i][move-1])
                board[i][move-1] = 0
                break
        
        if len(box) >= 2:   
            if box[-1] == box[-2]:
                box.pop(-1)                     # box = box[:-2] 를 다르게 코딩
                box.pop(-1)                     # pop()를 2번 사용해 stack(box)의 마지막 2개의 값 삭제
                count += 2
    
    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
