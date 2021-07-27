"""
Test Good
"""
def solution(N, stages):
    failRates = []
    for i in range(1,N+1):              # 스테이지 1 ~ N+1
        nowStage = 0                
        passStage = 0

        for stage in stages:    
            if i == stage:      
                nowStage += 1           # 현재 스테이지에 있는 사람
            if stage >= i :
                passStage += 1          # 현재스테이지 + 통과한 사람
        
        if passStage == 0:
            failRates.append([i,0])     # 통과한 사람이 없을 경우 [스테이지, 수] 추가
        else:
            failRates.append([i, nowStage / passStage])
    
    failRates = sorted(failRates, key=lambda fail: fail[1], reverse=True)
    return [failRates[i][0] for i in range(len(failRates))]

print(solution(5, [2,1,2,6,2,4,3,3]))