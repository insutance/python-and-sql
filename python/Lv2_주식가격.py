def solution(prices):
    answer = []
    for i in range(len(prices)):            
        sec = 0                                 # for문을 새로 돌 때마다 sec = 0 으로 초기화                                 
        for j in range(i+1, len(prices)):       # i+1 부터 index를 돌면서 계산
            if prices[j] >= prices[i]:          # 가격이 떨어지지 않는다면(뒤에 나오는 값이 더 크다면) sec += 1
                sec += 1                        
            else:                               # 가격이 떨어진다면(뒤에 나오는 값이 더 작다면)
                sec += 1                        
                break                           # sec +=1 해준 후 break를 통해 두 번째 for문 중단
        answer.append(sec)                      # 위에서 구한 sec를 answer에 append

    return answer

print(solution([1,2,3,2,3]))
print(solution([1,1,1,1,1,1,1,1,11,1,1,1,1,1]))