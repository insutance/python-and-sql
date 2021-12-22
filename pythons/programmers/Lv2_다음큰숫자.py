def solution(n):
    cnt = bin(n).count('1')             # bin()과 count()를 사용해 2진수 변환 후 1의 개수 카운팅
    while True:
        n += 1                          
        if cnt == bin(n).count('1'):    # n을 +1하면서 2진수 1의 개수를 카운팅 후, cnt와 비교
            break
    
    return n

print(solution(78))