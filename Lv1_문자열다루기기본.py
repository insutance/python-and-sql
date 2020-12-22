def solution(s):
    if not (len(s) == 4 or len(s)==6):
        return False
    return s.isnumeric()

print(solution('a234'))
print(solution('1234'))

# isnumeric() 을 사용해 숫자인지 판별함
# isalpha() = 문자열이 영어로 되어있는지 판별(한글도 영어로 취급함)
# isdigit() = 문자열이 숫자인지 판별 (numeric()함수보다는 더 작은 부분..?)

# isdigit()은 제곱이나 세제곱 표현 된 특수기호까지 인정을 해준다.
# isnumeric()은 제곱근 및 분수, 거듭제곱 특수문자까지 모두 인정을 해준다.
# isnumeric > isdigit 느낌

# isdecimal() 도 있지만 isdigit()보다 작은 느낌이라 사용하지 않으려고 함.