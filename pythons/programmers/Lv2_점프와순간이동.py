def solution(n):
    power = 1           # 무조건 1칸은 가야하므로 건전지 사용량 1로 초기화
    while True:
        if n == 1:      
            break
        # 2로 나눴을 때 나누어 떨어지면 순간이동이 가능함.
        power += n%2    # n%2 에서 나머지 값을 계속해서 사용량에 더해준다.
        n = n//2        # n은 계속해서 n//2 를 통해 몫을 넣어준다.
    
    return power

def solution2(n):
    return bin(n).count('1')    # 2진수로 바꾼 후 1의 갯수를 카운팅

print(solution(5))
print(solution(6))
print(solution(5000))
