"""백준 ATM"""
#1. sort()를 사용해 작은 값부터 앞에 오도록 만들어 준다.
#2. 반복문을 1부터 실행시켜 현재 값(i)과 이전 값(i-1)을 더해 현재 time[현재 index]에 넣어준다.
#3. sum()을 사용해 time의 모든 값을 더해준다.

"""main"""
# time : 16 
n = int(input())
time = list(map(int, input().split()))

time.sort()
for i in range(1,n):
    time[i] = time[i-1] + time[i]

print(sum(time))


"""main2"""
# time : 3
# 위의 코드보다 속도면에서 더 빠름. 하지만 워낙 작은 차이여서 큰 차이는 없어보임

n = int(input())
time = list(map(int, input().split()))

time.sort()
cur = 0
sum_value = 0
for ts in time:
    cur += ts
    sum_value += cur

print(sum_value)