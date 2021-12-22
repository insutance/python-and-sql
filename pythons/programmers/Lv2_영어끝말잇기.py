def solution(n, words):
    used_words = []
    number, order = 0,0

    used_words.append(words[0])
    last_word = words[0][-1]
    for i in range(1,len(words)):
        if words[i] not in used_words and words[i][0] == last_word:
            used_words.append(words[i])
            last_word = words[i][-1]
        else:
            number = (i%n)+1
            order = (i//n)+1
            break
    
    return [number, order]

"""
다른 사람의 코드
#1. 빈 리스트에 값을 저장할 필요가 없다.
#2. last_word라는 변수에 값을 저장할 필요 없이 words[i-1][-1] 로 비교를 하면 된다.
"""
def solution2(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            return [(i%n)+1, (i//n)+1]
    else:
        return [0,0]


print(solution2(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution2(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution2(2, ["hello", "one", "even", "never", "now", "world", "draw"]))