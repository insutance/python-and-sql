def solution(x,n):
    return [x * (i+1) for i in range(n)]

print(solution(2,5))
print(solution(4,3))
print(solution(-4,2))