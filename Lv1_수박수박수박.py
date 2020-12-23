def solution(n):
    answer = ''
    if n % 2 != 0:
        answer += "수"
        for i in range(3, n+1, 2):
            answer += "박수"
    else:
        for i in range(2, n+1, 2):
            answer += "수박"
    return answer

# 홀수일 때는 우선 "수"로 시작하게 한 후
# for문을 3부터 2씩 증가하면서 "박수"를 더해준다
# 짝수일 때는 2부터 2씩 증가하면서 "수박"을 더해준다.

"""
더 쉽게 푼 코드
#1. 우선 
"""
def solution1(n):    
    answer = "수박" * n
    print(answer)
    return answer[:n]

print(solution1(3))
print(solution1(4))