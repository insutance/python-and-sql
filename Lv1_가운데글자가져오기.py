def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[int(len(s)/2)]
    else:
        index = int(len(s)/2)
        answer = s[index-1:index+1]
        
    return answer

# 짝수일 때, 홀수일 때를 분리해서 생각함

"""
몫을 구할때는 '//' 연산자를 통해서 몫만 가져올 수 있음.
위의 코드는 int()로 강제변환을 해줬지만 그렇게 할 필요가 없었음.
"""
def solution2(s):
    answer = ''
    if len(s) % 2 == 1:
        answer = s[len(s)//2]
    else:
        index = len(s)//2
        answer = s[index-1:index+1]
        
    return answer