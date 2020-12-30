def solution(n):
    array = list(str(n))
    for i in range(len(array)):
        array[i] = int(array[i])
    
    return sum(array)

print(solution(123))

# 정수를 문자열로 변환 후 리스트로 만들어줬다.
# 리스트에 있는 것들은 지금 문자열이니, 다시 정수형으로 변환해준다.
# sum()을 통해 다 더해준다

"""
위의 코드를 한 줄로 코딩하기.

def solution2(n):
    return sum([int(num) for num in str(n)])
"""