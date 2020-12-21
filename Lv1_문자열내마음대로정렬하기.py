def solution(strings, n):
    strings.sort()
    
    array = []
    for string in enumerate(strings):
        array.append([string[1][n], string[0]])
    
    array.sort()
    
    answer = []
    for x in array:
        answer.append(strings[x[1]])
    
    return answer

print(solution(['sun', 'bed', 'car'], 1))

# n인덱스 값이 같을 경우 사전순서대로 정렬해야하므로
# 우선 처음에 strings를 sort()해준다.
# array에는 n인덱스 값과, string 인덱스 값을 같이 넣어준다.
# array sort() 후 (= n번째 인덱스로 sorting), 배열의 첫번째 값으로 정렬됨
# array[1] 값은 strings의 인덱스 값이므로 그것을 answer 배열에 추가

"""
찾아보니 sorted() 함수는 key 값이 존재함.
key값을 통해 정렬을 할 수 있다.

def solution(strings,n):
    return sorted(strings, key=lambda x: x[n])
"""