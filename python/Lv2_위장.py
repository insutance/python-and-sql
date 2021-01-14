def solution(clothes):
    dic = {}                        
    for item in clothes:
        if item[1] in dic.keys():   # item[1] = '옷 종류'
            dic[item[1]] += 1       # 옷 종류가 이미 dic에 있다면, (해당 옷 + 1)
        else:
            dic[item[1]] = 1        # 옷 종류가 dic에 없다면, 추가하면서 1로 초기화

    answer = 1
    for value in dic.values():      
        answer *= (value + 1)       # 이 부분이 핵심! (+1)한 값을 곱해준다.
    
    return answer - 1               # 안 입는 경우는 없으므로 -1 해준다.(= 하나는 반드시 선택해야 하므로)


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
# result : 5

print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
# result : 3