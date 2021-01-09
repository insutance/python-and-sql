def solution(priorities, location):
    queue = [[priorities[i], i] for i in range(len(priorities))]    # [값, 인덱스값] 을 배열로 만든다.
    stack = []

    while len(queue) > 0:                           # queue의 길이가 0이 될 때가지 반복문 실행
        if queue[0][0] == max(priorities):     
            stack.append(queue[0])                  # 2차배열의 [0][0] 값이 max값과 같다면 stack(=answer)에 저장
            del queue[0]                            # 저장한 값은 queue에서 삭제
            priorities[priorities.index(max(priorities))] = 0   # max값은 0으로 바꿔준다
        else:
            tmp = queue[0]                          # max값과 다르다면 queue의 맨 뒤로 보낸다.
            del queue[0]
            queue.append(tmp)
        
    for i in range(len(stack)):                     # stack(=answer)길이 만큼 반복문을 돌면서
        if stack[i][1] == location:                 # location(내가 요청한 문서)와 index가 같다면 return
            return i+1

print(solution2([2,1,3,2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))