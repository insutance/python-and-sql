def solution(nums):
    # len(nums)//2      : 골라야 하는 폰켓몬 수
    # len(set(nums))    : 중복값을 제외한 폰켓몬 종류의 수

    if len(nums)//2 < len(set(nums)):       
        return len(nums)//2
    else:
        return len(set(nums))

def solution2(nums):
    return min(len(nums)//2 , len(set(nums)))

print(solution([3,3,3,2,2,2]))