def solution(numbers):
    answer = []
    for x in range(0, len(numbers)):
        for y in range(x+1, len(numbers)):
            sum = numbers[x] + numbers[y]
            answer.append(sum)
    
    answer = list(set(answer))
    answer.sort()

    return answer

# 이중 for문을 사용해 배열 순서대로 더하기
# append()를 사용해 배열에 추가
# set()을 사용해 중복값 제거 => 리스트로 변환되지 않음
# list()를 통해 다시 데이터 타입을 list로 만들어줘야 함
# sort()를 사용해 배열 순서대로 정렬