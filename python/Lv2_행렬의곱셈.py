def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp_arr = []
        for j in range(len(arr2[0])):
            tmp = 0
            for z in range(len(arr1[0])):
                tmp += arr1[i][z] * arr2[z][j]
            tmp_arr.append(tmp)
        answer.append(tmp_arr)
    
    return answer

# 한 줄 코딩
def solution2(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]

print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))

