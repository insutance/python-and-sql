def get_divisor(num):                           # 약수 구하는 함수 list를 리턴
    divisor = []
    for i in range(1, int(num**0.5)+1):         
        if num % i == 0:
            divisor.append([i, num//i])
    return divisor

def solution(brown, yellow):
    yellow_list = get_divisor(yellow)           # yellow_list = 약수로 이루어진 2차배열

    for row, col in yellow_list:
        if ((row+2)*2) + (col*2) == brown:      # 갈색은 노란색의 테두리이기 때문에 테두리 개수를 구하는 식이 brown 개수와 같다면
            return [col+2, row+2]               # row,col에 +2 해준 후 리턴 (col >= row)
        

"""
함수 없이 짠 코드
"""
def solution2(brown, yellow):                   
    for i in range(1, int(yellow**0.5)+1):      # 약수를 구하기 위해 sqrt(yellow) 값을 해준다.
        if yellow % i == 0:                     # 해당 값이 약수라면
            row, col = i, yellow//i             # row 에는 약수를 col 에는 곱했을 때 yellow값이 나오는 수를 넣어준다.
            if ((row+2)*2) + (col*2) == brown:  # 갈색은 노란색의 테두리이기 때문에 테두리 개수를 구하는 식이 brown 개수와 같다면
                return [col+2, row+2]           # row,col에 +2 해준 후 리턴 (col >= row)


print(solution2(10,2))      # result : [4,3]
print(solution2(8,1))       # result : [3,3]
print(solution2(24,24))     # result : [8,6]