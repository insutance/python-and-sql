"""
처음 작성한 코드 (시간초과 및 효율성 안 좋음)
"""
def prime_number(number):
    if number != 1:
        for x in range(2, number):
            if number % x == 0:
                return False
    else:
        return False
    
    return True

def solution1(n):
    answer = 0    
    for number in range(1,n+1):
        if prime_number(number):
            answer += 1
    return answer


"""
'에라토스테네스의 체' 알고리즘
"""
import math

def solution(n):
    array = [False,False] + [True for i in range(n-1)]
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    answer = array.count(1)
    return answer

# 0,1 은 False로 나머지 n까지의 수는 True로 배열을 만든다.
# False = 소수가 아니라는 뜻
# 2~제곱근 값까지 for문을 돌면서 배수인 것들을 False로 변경해준다.
# True는 1과 같으므로 array.count(1) 을 해줘서 소수(True)의 개수를 찾는다.

"""
set()을 사용하여 문제해결
"""
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# 차집합을 통해 해결하는 코드
# 2~n 까지의 집합 num을 생성
# 만약 num 안에 i 값이 있다면(= i가 삭제되지 않았다면)
# 배수의 값들을 빼준다 num -= set(range(2*i, n+1, i))