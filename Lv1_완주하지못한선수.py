def solution1(participant, completion):
    completion.sort()
    participant.sort()

    i = 0
    while True:
        if i > len(completion)-1:
            return participant[i]

        if participant[i] != completion[i]:
            return participant[i]
        
        i += 1

# 리스트를 정렬 후 두 리스트에서 순서가 다른 원소가 있으면 그 원소는 완주하지 못한 선수
# sort()함수를 통해 정렬
# 무한루프를 통해 계속해서 비교
# i 가 완주자 리스트보다 커지면 마지막 남은 사람이 완주하지 못한 선수


"""
Counter 를 사용하는 방법
#1 collections.Counter() 의 결과값은 딕셔너리 형태이다.
"""
import collections

def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
