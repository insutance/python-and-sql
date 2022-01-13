"""
Link: https://www.acmicpc.net/problem/5430

- datas 입력을 받을 때 '[', ']', ',' 문자를 제거.
- R 입력을 받았을 때 reverse() 함수를 계속 실행시키면 시간 초과 발생.
  - R 입력을 받을 때 2개의 값이 변환되도록 한다.
    1. 왼쪽에서 데이터 제거할건지 vs. 오른쪽에서 데이터 제거할건지
    2. reverse_count 가 짝수이면 원상태, 홀수이면 reverse() 실행하도록 하기 위해 +1 을 해주기.
- D 입력을 받았을 때 pop(), pop(0) 을 사용해 데이터 제거.
- 빈 배열이라도 "error" 출력이 아니라면 "[]" 를 출력해야 함.
"""

T = int(input())
for _ in range(T):    
    funcs = list(input())
    n = int(input())
    datas = input()[1:-1].split(",")
    
    if datas==[""]:
        datas = []
    
    reverse_count = 0
    is_left = True
    is_error = False

    for func in funcs:
        if func == "R":
            is_left = not is_left
            reverse_count += 1
        elif func == "D" and datas:
            if is_left:
                datas.pop(0)
            else:
                datas.pop()
        elif func == "D" and not datas:
            is_error = True
            break
    
    if reverse_count % 2 !=0:
        datas.reverse()

    if datas:
        print(f"[{','.join(datas)}]")
    elif not datas:
        if is_error:
            print("error")
        else:
            print(datas)