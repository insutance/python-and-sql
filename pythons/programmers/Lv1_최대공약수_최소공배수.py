from math import gcd

def solution(n,m):
    _gcd = gcd(n,m)
    _lcm = (n * m) // _gcd

    return [_gcd, _lcm]

# 최대공약수(Greatest Common Divisor) : 두 수의 약수들 중 최대값
# 최소공배수(Least Common Multiple) : 두 수의 곱에서 두 수의 최대공약수를 나눈 것과 같다.