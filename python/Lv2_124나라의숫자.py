def solution(n):
    # 3진법으로 풀게되면 0이 생기기 때문에 문자열 '124'를 통해 계산함
    # n%3==0 일때는 1 // n%3==1 일때는 2 // n%3==2 일때는 4 삽입되도록 함
    answer = ''                             
    while n > 0:
        n -= 1                          # 몫에서 -1을 해줌으로써 loop를 한번 더 안 돌게 한다.
        answer = '124'[n%3] + answer    # 문자열('124')에서 3개의 숫자중 하나를 answer에 더해준다.
        n //= 3                         # 3진법 계산으로 //3을 통해 몫을 넣어준다.
    return answer


print(solution(20))
