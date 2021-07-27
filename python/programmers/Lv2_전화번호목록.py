def solution(phone_book):
    phone_book.sort()                           # 접두어를 판단하면 되는 것이므로 sort()를 통해 정렬함.
    for i in range(len(phone_book)):    
        for j in range(i+1, len(phone_book)):   # 2번 줄에서 sort()를 했기 때문에 i+1부터 뽑아와도 됨.
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:     # 접두어를 판단하면 되는 것이기 때문에 [:접두어길이] 와 같은지 판단
                return False
    return True

print(solution(['119', '97674223', '1195524421']))  # False
print(solution(["1195524421", '119', '97674223']))  # False
print(solution(["123", "456", "789"]))              # True
print(solution(['12','12','1235','567','88']))      # False