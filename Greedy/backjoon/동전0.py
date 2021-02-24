"""백준-동전0"""

""" main1 """
# time : 20
n, k = map(int, input().split())
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

result = 0
coin_types.sort(reverse=True)      
for i in range(n):
    result += k // coin_types[i]
    k %= coin_types[i]

print(result)


""" main2 """
# time : 7
n, k = map(int, input().split())
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

result = 0
for i in range(n):
    coin = coin_types.pop()         
    result += k // coin
    k %= coin

print(result)


""" main3 """
# time : 1
n, k = map(int, input().split())
coin_types = []
for i in range(n):
    coin_types.append(int(input()))

result = 0
coin_types.reverse()               
for i in range(n):
    result += k // coin_types[i]
    k %= coin_types[i]

print(result)