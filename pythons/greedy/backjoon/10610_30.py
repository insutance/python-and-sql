"""
Link: https://www.acmicpc.net/problem/10610

- 30의 배수는 3의 배수이면서 10의 배수여야 한다.
- 3의 배수: 각 자리수의 합이 3의 배수여야 한다.
- 10의 배수: 일의 자리 값이 반드시 1이여야 한다.
"""

# 정답 코드
n = input()
nums = list(map(int, n))

if 0 not in nums or sum(nums) % 3 != 0:
    result = -1
else:
    nums.sort(reverse=True)
    result = "".join(map(str, nums))

print(result)


# 값은 나오지만, 메모리 초과 발생 코드
from itertools import permutations

n = input()
nums = list(map(int, n))

if 0 not in nums:
    result = -1
else:
  nums.sort(reverse=True)
  num_of_cases = list(permutations(nums))

  result = -1
  for case in num_of_cases:
      num = int("".join(map(str, case)))
      if num % 30 == 0:
          result = num
          break

print(result)
