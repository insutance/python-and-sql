import heapq

"""
scoville 배열 크기가 작다면 괜찮다.
하지만 배열 크기가 커진다면 효율성 문제 탈락
"""
def solution(scoville, K):
    count = 0
    while len(scoville) > 1:
        if min(scoville) >= K:
            return count
        scoville.sort()
        a,b = scoville.pop(0), scoville.pop(0)
        scoville.append(a + (b*2))
        count += 1

    if scoville.pop() >= K:
        return count

    return -1

"""
내가 작성한 정답 코드
"""
def solution2(scoville, K):
    import heapq
    
    count = 0
    heapq.heapify(scoville)     # 기존 리스트를 힙으로 변환

    while len(scoville) > 1:    # 2개 이상있어야 pop을 2번 할 수 있기 때문에 조건 설정
        if scoville[0] >= K:    # heapq[0] = 최소값 , 최소값이 K와 같거나 K보다 크다면 return
            return count
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)
        heapq.heappush(scoville, a+(b*2))
        count += 1

    if scoville[0] >= K:        # scoville길이가 1일 때 상황
        return count

    return -1                   # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없을 때 -1 return

"""
좀 더 깔끔한 코드
"""
def solution3(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
    

print(solution2([1, 2, 3, 9, 10, 12], 7))    # result : 2