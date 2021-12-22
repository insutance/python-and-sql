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

"""
정말 힘들었던 문제다...
#1. 우선 remove를 사용해서 lost배열을 계속해서 지워나갔지만
    마지막 1개가 남았을 때 .remove()함수를 사용하면 제거되지 않는다.

#2. 그래서 내가 한 방법은 그 값이 있다면 지장을 주지 않는 값으로 변경한 후
    count ++ 하는 것이다.
"""