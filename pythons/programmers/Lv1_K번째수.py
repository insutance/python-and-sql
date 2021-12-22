def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i = commands[n][0] - 1
        j = commands[n][1]
        k = commands[n][2] - 1
        
        new_array = array[i:j]
        new_array.sort()
        answer.append(new_array[k])

    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

# commands의 길이만큼 for문을 돌게함.
# 배열의 값을 i,j,k 에 넣어줌.
# 배열을 자르고, 정렬한 후 새로운 배열에 추가

"""
for문에서 in commands를 함으로써 하나의 배열을 꺼냄.
command 값을 i,j,k = command 를 통해서 한 줄에 값을 넣어준다.

list.sort() 와 sorted(list) 차이점
#1. sort() 함수는 원본 리스트를 변경하는 것이고, 반환값은 None이다.
#2. sorted() 함수는 원본 리스트를 변경하는 것은 아니다. 새로운 배열을 만들어내는 것이다.
"""
def solution2(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer