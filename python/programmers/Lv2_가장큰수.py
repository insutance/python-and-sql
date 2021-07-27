def solution(numbers):
    #0. key point
    numbers_str = [str(num) for num in numbers]                 #1. 사전 값으로 정렬하기
    numbers_str.sort(key=lambda num: num*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교

    return str(int(''.join(numbers_str)))
    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.

print(solution([6, 10, 2]))             # result : 6210
print(solution([3, 30, 34, 5, 9]))      # result : 9534330
print(solution([0,0,0,0]))              # result : 0