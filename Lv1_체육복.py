import collections

def solution(n, lost, reserve):
    count = 0
    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = -1
            count += 1
    
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            lost[i] = -1
            count += 1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            lost[i] = -1
            count += 1
            
    answer = (n - len(lost)) + count
    return answer

print(solution(	5, [1,3,5], [1,3,5]))