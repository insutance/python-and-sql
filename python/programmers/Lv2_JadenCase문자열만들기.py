def solution(s):
    answer = []
    for word in s.lower().split(" "):       # ' ' 기준으로 데이터를 분리
        answer.append(word.capitalize())    # caplitalize()를 통해 앞 문자만 대문자로 변경
    return " ".join(answer)                 # join()을 사용해 리스트를 문자열로 변경

def solution2(s):
    return " ".join(i.capitalize() for i in s.lower().split(" "))

print(solution("  test  TTTs "))   # result: '  Test  Ttts '