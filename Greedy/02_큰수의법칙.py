"""
이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_93'
"""

"""
핵심내용
#1. 배열 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
#2. 가장 큰 수를 K번 더하고 두 번째로 큰 수를 1번 더하는 연산을 반복한다.
"""

"""
내가 작성한 코드
#1. 배열 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
#2. k로 나누어 떨어지지 않는다면 가장 큰수를 계속해서 더한다.
#3. k로 나누어 떨어지면 두 번째로 큰 수를 1번 더해준다.
"""
def solution(data, m, k):
    result = 0
    
    data.sort()

    for i in range(1,m+1):
        if i%k != 0:
            result += data[-1]
        else:
            result += data[-2]

    return result

print(solution([2,4,5,4,6], 8, 3))
print(solution([3,4,3,4,3], 8, 3))


"""
입력값까지 직접 받아오는 코드
"""
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    
    if m == 0:
        break
    result += second
    m -= 1

print(result)