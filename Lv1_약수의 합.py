def solution(n):
    answer = list()
    array = [i for i in range(1, n//2)]
    for i in array:
        if n % i == 0:
            answer.append(i)
            answer.append(n//i)
    
    answer = sum(list(set(answer)))

    return answer

print(solution(3000))

## 테스트 코드 1개가 오류가 계속 발생했다.
## 정확한 원인을 찾지 못하겠다... 어떤 테스트에서 오류가 발생하는지...
# 우선 주어진 n(정수) 의 //2 를 해줘서 반 넘는 값은 필요가 없다.
# 만든 array를 for문을 통해 돌면서 n%i==0 이면 i값과, n//i(몫)을 answer에 넣어준다
# 만들어진 answer배열을 sum()을 통해 더해준다.

"""
#1. solution2 함수를 사용해 문제를 해결했다..
    하지만 좋은 코드라고 생각하지는 않는다.
    n=3000 이라면, 3000번을 돌게 되므로 좋은 코드가 아니라고 생각한다.

def solution2(n):
    return sum([i for i in range(1, n+1) if n % i == 0])
"""