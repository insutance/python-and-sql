def solution(answers):
    supoja1 = [1,2,3,4,5]
    supoja2 = [2,1,2,3,2,4,2,5]
    supoja3 = [3,3,1,1,2,2,4,4,5,5]
    
    supoja1_cnt, supoja2_cnt, supoja3_cnt = 0,0,0
    
    for i in range(0,len(answers)):
        x = i % len(supoja1)
        y = i % len(supoja2)
        z = i % len(supoja3)
        
        if answers[i] == supoja1[x]:
            supoja1_cnt += 1
        if answers[i] == supoja2[y]:
            supoja2_cnt += 1
        if answers[i] == supoja3[z]:
            supoja3_cnt += 1
    
    answer = []
    maxNum = max(supoja1_cnt, supoja2_cnt, supoja3_cnt)
    if maxNum == supoja1_cnt:
        answer.append(1)
    if maxNum == supoja2_cnt:
        answer.append(2)
    if maxNum == supoja3_cnt:
        answer.append(3)
    
    return answer

solution([1,2,3,4,5])
solution([1,3,2,4,2])

# 각 수포자의 패턴은 따로 배열을 생성
# count = 0 으로 생성
# 각 패턴에 맞는 인덱스를 % 를 통해서 x,y,z 생성
# 3명 중 max 값을 구한 후 그 값과 동일하다면 answer 배열에 추가 후 리턴

"""
enumerate
#1. 반복문 사용시 몇 번째 반복문인지 확인이 필요할 때 사용
#2. 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환

ex)
t = [1,5,7,33,39,52]
for p in enumerate(t):
    print(p)

result
>>
(0,1)
(1,5)
(2,7)
(4,39)
(5,52)
"""