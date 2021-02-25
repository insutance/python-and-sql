"""백준-잃어 버린 괄호"""
"""
#1. 마이너스를 만날 때 가장 큰 수를 빼면 된다.
#2. 조건 중 '연속해서 두 개의 연산자가 나타나지 않고' 라는 말이 있다.
    => '-'가 나오면 그 뒤에는 '+'라는 말이다. 
    => '-' 만났을 때 다음 2개를 더해주면 '가장 큰 수'
#3. i > 0 이상 부터는 계속해서 더해준 값을 빼준다.
    => 원래 '-' 자리이다.
"""
data = input().split('-')

result = 0
for i in range(len(data)):
    data[i] = sum(map(int, data[i].split('+')))
    if i == 0:
        result = data[i]

    if i > 0:
        result -= data[i]

print(result)