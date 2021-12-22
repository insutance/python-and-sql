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
#1. 우선 "수박" 문자열을 n 만큼 만들어준다
#2. 3을 입력했다면 answer = "수박수박수박" 
#3. 하지만 Return을 할 때 [:3] 을 해줌으로써
    문자열에서 0,1,2 만 리턴되도록 한다.
"""
def solution1(n):    
    answer = "수박" * n
    return answer[:n]