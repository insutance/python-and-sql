"""
Link: https://www.acmicpc.net/problem/1032
"""

# 첫 생각
# 우선 모든 단어들을 입력받은 후, 계산
# 첫번째 단어를 기준으로 생각
# set()을 사용, 길이가 1개보다 많다면 다른 단어가 존재한다는 뜻이므로 "?" 추가
n = int(input())

files = []
for _ in range(n):
    files.append(input())

pattern = ""
for i in range(len(files[0])):
    alphabets = set()
    for file in files:
        alphabets.add(file[i])

    if len(alphabets) > 1:
        pattern += "?"
    else:
        pattern += alphabets.pop()

print(pattern)


# 두번째 생각
# 첫번째 단어를 기준으로 생각
# 입력 받을때 str -> list 변경
# 단어들을 입력 받으면서 계산
n = int(input())
first_words = list(input())

for i in range(n - 1):
    other_words = list(input())
    for j in range(len(first_words)):
        if first_words[j] != other_words[j]:
            first_words[j] = "?"

print("".join(first_words))
