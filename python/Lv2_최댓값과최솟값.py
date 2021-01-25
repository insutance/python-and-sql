def solution(s):
    # split()을 통해 공백 기준으로 나눠 리스트를 생성
    # map()을 사용하여 값을 str -> int 로 변경
    # map object를 list()를 통해 리스트로 변경
    arr = list(map(int, s.split(' ')))         
    arr.sort()                                  # int로 이루어진 배열을 sort
    return str(arr[0]) + " " + str(arr[-1])     # 첫번째 값 : 최솟값, 마지막 값 : 최댓값

"""
min, max 사용
"""
def solution2(s):
    arr = list(map(int, s.split(' ')))
    return str(min(arr)) + " " + str(max(arr))