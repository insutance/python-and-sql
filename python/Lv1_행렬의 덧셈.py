def solution(arr1, arr2):
    answer = []                         
    for i, arr in enumerate(arr1):                  # 행과 열의 크기가 같으므로 arr1을 기준으로 함.
        new_arr = []                                # 새로운 배열을 answer에 추가하기 위해 빈 배열 생성
        for j in range(len(arr)):                   
            new_arr.append(arr1[i][j]+arr2[i][j])   # arr1, arr2의 값을 new_arr 배열에 추가
        answer.append(new_arr)                      # 새로 생성된 new_arr를 answer에 추가

    return answer

def solution2(arr1,arr2):
    answer = []
    for a,b in zip(arr1,arr2):      # zip()함수를 통해 두 배열의 값을 가져오기
        arr = []                    # 새로운 배열을 answer에 추가하기 위해 빈 배열 생성
        for c,d in zip(a,b):       
            arr.append(c+d)
        answer.append(arr)
    return answer

print(solution2([[1,2],[2,3]], [[3,4],[5,6]]))