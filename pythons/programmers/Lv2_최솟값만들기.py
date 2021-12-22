def solution(A,B):
    A.sort(reverse=True)            # A 배열은 큰 수가 앞쪽에 위치하도록 정렬
    B.sort()                        # B 배열은 큰 수가 뒤쪽에 위치하도록 정렬

    sum = 0
    for i in range(len(A)):         # 같은 배열이므로 A or B 배열 2개 중 하나의 길이로 반복문
        sum += A.pop() * B.pop()    # A와B 배열에서 마지막 값들 하나씩 뽑아와 곱한 후 sum에 더한다.
    
    return sum

"""
zip()을 사용한 코드 (pop()보다 조금 더 빠름)
"""
def solution2(A,B):
    A.sort()
    B.sort(reverse=True)

    sum = 0
    for a,b in zip(A,B):
        sum += a*b
    
    return sum

print(solution([1,4,2], [5,4,4]))   # result : 29
print(solution([1,2], [3,4]))       # result : 10
