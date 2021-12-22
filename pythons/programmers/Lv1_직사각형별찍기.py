def solution(n,m):
    for i in range(m):              # for문을 통해 enter역할
        print('*'*n)   

def solution2(n,m):
    answer = ('*'*n + '\n') * m     # 개행문자까지 추가해 그것을 그대로 print
    print(answer)

print(solution(5,3))