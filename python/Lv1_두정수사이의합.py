def solution(a, b):
    array = [a,b]
    array.sort()
    
    answer = 0
    for num in range(array[0], array[1]+1):
        answer += num
    
    return answer
# 두 수를 배열로 만들어 sort()를 사용해 정렬
# for문을 통해 더한 값 return


"""
아래가 더 좋은 코드라고 생각함.
#1. sum() 함수 사용
"""
def solution2(a, b):
    answer = sum(range(min(a,b), max(a,b)+1))
    return answer