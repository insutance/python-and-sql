def solution(people, limit):    
    people.sort()               # 배열 정렬

    count = 0
    i, j = 0, len(people)-1     # index 저장(0, 마지막 인덱스)
    while i < j:
        # (제일 작은 값 + 제일 큰 값)이 limit 값보다 작다면 i,j 변경
        if people[i]+people[j] <= limit:
            i += 1     
            j -= 1
        # (제일 작은 값 + 제일 큰 값)이 limit 값보다 크다면 큰 값(j)만 변경
        else:
            j -= 1
        
        count += 1

        # 같은 인덱스를 가리키고 있다면 count+=1 한 후 break
        if i==j:
            count += 1
            break

    return count

print(solution([70,50,80,50], 100))     # 3
print(solution([70,80,50], 100))        # 3
print(solution([20,50,50,70,80], 100))  # 3
print(solution([40,70,70,90], 100))     # 4

"""다른 사람 풀이1"""
def solution2(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer

"""다른 사람 풀이2"""
def solution3(people, limit):
    answer = 0
    poo = sorted(people)
    while poo:
        if len(poo) == 1:
            answer += 1
            break
        if poo[0] + poo[-1] > limit:
            poo.pop()
            answer += 1
        else:
            poo.pop(0)
            poo.pop()
            answer += 1
    return answer
