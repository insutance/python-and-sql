def solution(arr):
    answer = 0
    n = 1                           
    
    while True:
        answer = max(arr) * n       # 가장 큰 수의 배수 기준으로 최소공배수를 구함.
        result = True               # if result=True: 최소공배수    else: 최소공배수가 아님
        for num in arr:
            if answer % num != 0:   
                result = False      # answer가 나누어 떨어지지 않으면 result=False로 변경 후 break
                break
        if result:                  # result 판별 True이면 while True문을 빠져나옴
            break                   
        n += 1
        
    return answer

def solution2(arr):
    from math import gcd                            # 최대공약수를 구하는 gcd() import
    answer = arr[0]                                 # answer을 arr[0]으로 초기화

    for num in arr:                                 # 반복문을 처음부터 끝까지 돈다.
        #1. (arr[0],arr[1])의 최소공배수를 구한 후 answer에 저장
        #2. (1에서 구한 최소공배수, arr[2])의 최소공배수를 구한 후 answer에 저장
        #3. 모든 배열을 돌면서 최소공배수를 구하고, 저장하고 하는 방식을 진행
        answer = answer*num // gcd(answer, num)     

    return answer

print(solution2([2,6,8,14]))

