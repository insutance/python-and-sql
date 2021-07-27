"""백준-거스름돈"""
#1. 값이 큰 동전들부터 거스름돈 주기

money = 1000 - int(input())     # 1000엔 냈을 때의 거스름돈

coin_types = [500, 100, 50, 10, 5, 1]

result = 0
for coin in coin_types:
    result += money // coin
    money %= coin

print(result)