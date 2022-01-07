"""
Link: https://www.acmicpc.net/problem/13305

- 다음 주유소와 가격을 비교해 현재보다 다음 주유소 가격이 더 비싸다면 현재에서 더 많이 넣는게 좋다.
- 다른 말로 하면 현재에서 더 많이 넣지 말고, 다음 주유소 가격(비싼가격)을 현재 주유소 가격(저렴한가격)으로 만들어주면 된다.

- oil_prices 길이가 distances 길이보다 반드시 +1 이다.
- for문에서 len(oil_prices)가 아닌, len(distances)로 넣어줘야 한다.
"""

city_count = int(input())
distances = list(map(int, input().split()))
oil_prices = list(map(int, input().split()))

result_price = 0
for i in range(len(distances)):
    if oil_prices[i] <= oil_prices[i + 1]:
        oil_prices[i + 1] = oil_prices[i]
    result_price += oil_prices[i] * distances[i]

print(result_price)
