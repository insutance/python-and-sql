def solution(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

a = [1,2,3,4]
b = [-3, -1, 0, 2]
print(solution(a,b))


"""
#1. zip()을 사용해 계산하는 방법
    zip()은 '동일한 개수'로 이루어진 자료형을 묶어주는 역할을하는 함수

def solution2(a,b):
    answer = 0
    for x,y in zip(a,b):
        answer += x*y
    return answer
"""