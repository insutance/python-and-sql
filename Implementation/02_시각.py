# 이것이 취업을 위한 코딩 테스트다 with 파이썬 'page_113'

# 문제유형 : 완전 탐색
# 시간복잡도 : O(N^3)
# 단순히 시각을 1씩 증가하는 24x60x60 3중 반복문

"""내가 작성한 코드"""
n = int(input())
hour, minute, second = 0,0,0

count = 0
while True:
    if hour==n and minute == 59 and second==59:
        break
    
    second += 1

    if second > 59:
        minute += 1
        second = 0
        
    if minute > 59:
        hour += 1
        minute = 0

    if '3' in str(second) or '3' in str(minute) or '3' in str(hour):
        count += 1

print(count)


""" 답안 예시 """
n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)