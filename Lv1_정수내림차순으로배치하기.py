def solution(n):
    arr = sorted([num for num in str(n)], reverse=True)
    answer = "".join(arr)
    return int(answer)

print(solution(118372))

# 정수 n을 문자열로 변환후, 배열로 만들어준다.
# 배열을 만들 때 reverse=True 로 설정해 내림차순으로 정렬한다.
# join()을 활용해 배열을 문자열로 합치고
# int()로 변환해 return 한다.

"""
2번 째 줄을 아래와 같이 바꿀 수 있다.
arr = sorted(list(str(n)), reverse=True)
"""