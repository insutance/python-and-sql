def solution(numbers):
    answer = []
    for x in range(0, len(numbers)):
        for y in range(x+1, len(numbers)):
            sum = numbers[x] + numbers[y]
            answer.append(sum)
    
    answer = list(set(answer))
    answer.sort()

    return answer