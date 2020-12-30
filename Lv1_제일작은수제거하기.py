def solution(arr):
    arr.remove(min(arr))
    
    if not arr:
        return [-1]
    
    return arr

print(solution([4,3,2,1]))
print(solution([10]))

# 배열 arr 에서 가장 작은 수를 제거
# arr이 빈 배열이라면 [-1] return
# 그렇지 않으면 arr return