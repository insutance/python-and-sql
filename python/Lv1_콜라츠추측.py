def solution(num):
    for count in range(500):        # 작업은 최대 500번
        if num == 1:                # num 값이 1이 되는 순간 count 리턴
            return count
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        
    return -1

print(solution(6))