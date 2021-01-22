def solution(n):
    answer = []
    last_list = [n+i for i in range(n)]
    answer.append(last_list)
    for i in range(len(last_list)-1, 0, -1):
        tmp_list = [0 for j in range(i)]
        tmp_list[0] = i
        if tmp_list[-1] == 0:
            tmp_list[-1] = answer[-1][-1] + 1
        answer.append(tmp_list)
    
    answer.sort()
    for x in answer:
        print(x)
            

        

print(solution(4))