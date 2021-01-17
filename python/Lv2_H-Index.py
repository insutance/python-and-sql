def solution2(citations):
    # 문제의 핵심은 Index를 Return 하는 것이다.
    # 인용된 논문이 논문 수(sort한 citations의 Index값)와 같거나 논문 수보다 작아지기 시작하는 숫자가 바로 H-Index이다.
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i:           
            return i
    
    return len(citations)               # 같거나 작아지지 않는다면 citations의 길이(=인덱스 마지막) 리턴

            
print(solution([3, 2, 0, 6, 1, 5]))     # 3
print(solution([5, 3, 10, 4, 8]))       # 4
print(solution([25, 8, 5, 3, 3]))       # 3
print(solution([5,5,5,5]))              # 4
print(solution([7]))                    # 1