def solution(n):
    answer = []
    array = [int(num) for num in str(n)]
    for i in range(len(array)):
        answer.append(array[-1])
        del array[-1]
    
    return answer

print(solution(12340))

# reverse()가 생각이 안나서 짠 코드...
# 새로운 answer 배열에 array[-1] 것들을 계속해서 넣어주는 방식

"""
reverse() 사용한 코드

def solution2(n):
    array = [int(num) for num in str(n)].reverse()
    return answer
"""

"""
arr[::-1]  :    처음부터 끝까지 -1칸 간격으로(=역순으로)
arr[A:B:C] :    index A부터 idnex B까지 C의 간격으로 배열을 만들어라!

def solution3(n):
    return [int(num) for num in str(n)][::-1]
"""
