"""
Link: https://www.acmicpc.net/problem/5086

- 입력은 "여러 테스트 케이스"로 이루어져 있다. 라는 말에 주의를 해야한다.
- 한번 입력을 받는게 아니라 계속해서 입력을 받고 0 0 값을 받을 때까지 계속 코드가 실행되어야 한다는 말이였다.
"""

while True:
    data = list(map(int, input().split()))

    if data[0] == data[1]:
        break
    elif max(data) % min(data) == 0:
        if min(data) == data[0]:
            print("factor")
        else:
            print("multiple")
    else:
        print("neither")
