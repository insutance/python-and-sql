import math
def solution(n):
    if math.sqrt(n) % int(math.sqrt(n)) == 0:
        answer = (int(math.sqrt(n)) + 1)**2
    else:
        answer = -1
    
    return answer

print(solution(121))

# sqrt() 을 사용하기 위해서 math 를 import 한다.
# sqrt(n)과 int(sqrt(n)) 값을 % 연산자로 계산해 값이 0 이면
# 양의 정수라고 판단

"""
나머지 값이 있는지 없는지만 판단하는 것이기 때문에.
3번째 코드를 아래오 같이 변경하는게 좋을 것 같다.

>> if math.sqrt(n) % 1 == 0:
"""