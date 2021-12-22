def solution(s):
    cnt, cnt_zero = 0,0             # 이진변환(cnt), 0 제거 갯수(cnt_zero)
    while True:
        if s == '1':                # 만약 s가 '1'이라면 break
            break
        
        cnt += 1                    # 이진변환 카운트 +1
        cnt_zero += s.count('0')    # count()를 사용해 제거할 '0'의 갯수 카운팅
        s = s.replace('0','')       # replace()를 사용해 '0' -> ''으로 변경
        s = bin(len(s))[2:]         # bin()을 사용하면 '0b'가 나오기 때문에 [2:]를 사용해 숫자만 나오도록 함

    return [cnt, cnt_zero]

print(solution("1111111"))