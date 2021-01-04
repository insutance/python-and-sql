def solution(d, budget):
    while sum(d) > budget:
        d.remove(max(d))        # 배열에서 가장 큰 값을 계속해서 빼줌으로써 최대로 예산을 맞춤
    return len(d)
    
print(solution([1,3,2,5,4], 9))
print(solution([2,2,3,3], 10))