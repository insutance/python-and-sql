def solution(arr, divisor):
    answer = []
    for x in arr:
        if x % divisor == 0:
            answer.append(x)
    
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    
    return answer

"""
아래의 코드 부분을 더 좋아보이게 바꿔보자
(수정 전)
if len(answer) == 0 
    answer.append(-1)

(수정 후)
if not answer:
    answer = [-1]

빈 배열은 'false' 이다.
not 을 통해 빈 배열 체크를 할 수 있다.
"""