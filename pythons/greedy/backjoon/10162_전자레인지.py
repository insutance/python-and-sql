"""
Link: https://www.acmicpc.net/problem/10162

- 누른 횟수의 합은 항상 최소가 되어야 함
- 출력 값은 몫으로, 나머지 연산자를 사용해 다음 button 값에서 사용할 값을 저장
"""
sec = int(input())

buttons = [300, 60, 10]
result = []

if sec % 10 != 0:
    result = [-1]
else:
    for button in buttons:
        result.append(sec // button)
        sec %= button

print(" ".join((map(str, result))))


"""for문 사용하지 않고 그냥 print()문"""
sec = int(input())

if sec % 10 != 0:
  print(-1)
else:
  x = sec // 300
  y = (sec % 300) // 60
  z = ((sec % 300) % 60) // 10
  print(f"{x} {y} {z}")
