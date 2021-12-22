def solution(x):
    y = sum([int(num) for num in str(x)])   # 정수 x를 각 자리수 별로 나눈 배열로 생성후 sum()을 통해 총합계를 y에 넣어준다.
    if x % y == 0:
        return True
    else:
        return False

print(solution2(10))
print(solution2(12))
print(solution2(11))
print(solution2(13))

"""
한 줄로 코딩

def solution2(x):
    return x % sum([int(num) for num in str(x)]) == 0
"""