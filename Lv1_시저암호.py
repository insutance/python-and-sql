def solution(s, n):
    answer = ""
    for alpha in s:
        if alpha >= 'A' and alpha <= 'Z':
            num = (ord(alpha) + n) % 65
            if num > 25:
                answer += chr(ord('A') + (num - 26))
            else:
                answer += chr(ord('A') + num)

        elif alpha >= 'a' and alpha <= 'z':
            num = (ord(alpha) + n) % 97
            if num > 25:
                answer += chr(ord('a') + (num - 26))
            else:
                answer += chr(ord('a') + num)

        elif alpha == ' ':
            answer += ' '
    
    return answer

print(solution2("AB", 1))

# 알파벳 26개
# 대문자 : 65~90 // 소문자 : 97~122


"""
내가 짠 코드보다 더 좋은 코드
#1. 문자열을 list로 변환
#2. 대문자 소문자는 내가 푼 것처럼 범위설정이 아닌 isupper(), islower()를 사용

def solution2(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
        
    return "".join(s)
"""