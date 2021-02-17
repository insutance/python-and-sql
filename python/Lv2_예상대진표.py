def solution(n,a,b):
    count = 0           
    while a != b:   
        # '//' 연산자를 활용해 몫이 같으면 대결 상대이다.
        # 둘 중 어떠한 값이 1이 되더라도 (1+1)//2 를 해주기 때문에 계속해서 1에 머무를 수 있다.    
        a = (a+1)//2
        b = (b+1)//2

        count += 1
    
    return count
        
print(solution(8, 4, 7))
