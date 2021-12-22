"""백준 설탕배달"""
#1. 5kg에 설탕을 빠짐없이 담을 수 있다면 5로 나눈 몫을 출력 후 break
#2. 5kg에 설탕을 빠짐없이 담을 수 없다면 3kg 봉지에 한 번 담기(count 1증가, 입력값 3감소)
#3. 만약 입력값(n)이 0보다 작아지면 -1을 출력하고 break

"""main"""
n = int(input())

count = 0
while True:
    if n%5 == 0:
        count += n//5
        print(count)
        break
    
    count +=1
    n -= 3
    if n < 0:
        print(-1)
        break