def solution(s):
    answer = ''
    array = sorted(s,reverse=True)

    for alpha in array:
        answer += alpha

    return answer

print(solution('Zbcdefg'))

# sorted(s, reverse=True) 를 통해서 역순으로 정렬
# 이때 대문자는 소문자보다 작은 것으로 판단된다.
# sorted() 를 사용하면 문자열->리스트 로 변환이 되는데,
# 그것을 다시 문자열로 만들어 주기 위해
# for문으로 더해줬다.

"""
def solution(s):
    answer = ''.join(sorted(s,reverse=True))
    return answer

이렇게 더 간략하게 코딩할 수 있다.

#1. join() 을 사용해 "리스트->문자열" 로 만들어줄 수 있다.
#2. join() 앞에 ''.join() 이 붙는데, 이 안에 ':'.join() 이렇게 콜론을 넣게되면
    리스트의 각각이 문자열로 더해질 때 사이사이에 ':' 이 붙게 된다.
    '/'.join()을 하게되면 g/f/e/d/c/b/Z 이런식으로 결과가 나오게 되겠지.

#3. split() 은 "문자열->리스트" 로 만들어줄 수 있다.
    string.split() or string.split('/') 후자는 '/'를 기준으로 나누는 것을 의미하고
    기본은 공백을 기준으로 나누는 것을 의미한다.
"""