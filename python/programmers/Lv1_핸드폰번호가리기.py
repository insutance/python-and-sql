def solution(phone_number):
    # '*'문자는 phone_number에서 뒤에 4개를 뺀 숫자만큼 써주고, 나머지 값은 그대로 붙여주기.
    return '*' * (len(phone_number)-4) + phone_number[len(phone_number)-4:]

print(solution("01033334444"))
print(solution("027778888"))