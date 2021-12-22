"""
#1. 재귀호출을 사용해 작성한 코드
- '시간초과' 발생
"""
def solution(n):
    if n < 2:
        return n
    else:
        return (solution(n-1)+solution(n-2)) % 1234567

"""
#2. 배열을 사용해 직접 만들어주는 코드
"""
def solution1(n):
    answer = []
    for i in range(n+1):
        if i==0 or i==1:
            answer.append(i)
        else:
            f = answer[i-1] + answer[i-2]
            answer.append(f % 1234567)

    return answer[-1]

"""
#3. 2번 방법을 더 짧게 작성한 코드
"""
def solution2(n):
    answer = [0,1]
    for i in range(2,n+1):
        answer.append((answer[i-1] + answer[i-2]) % 1234567)
    
    return answer[-1]

"""
#4. 미친코드
"""
def solution3(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a

print(solution(10))
print(solution1(10))
print(solution2(10))
