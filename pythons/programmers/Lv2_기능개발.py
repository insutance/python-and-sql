def solution(progresses, speeds):
    days = []   
    for progress, speed in zip(progresses, speeds):
        day = 1                                         # day(배포 가능 날짜)를 1로 초기화
        while True:                                     
            if progress + (speed * day) < 100:          # 진도율이 100%보다 작다면
                day += 1                                # day +1
            else:                                       
                break                                   # 진도율이 100% 이상이라면 반복문 종료
        days.append(day)                                # days에 day(해당 배포 가능 날짜)를 추가

    answer = []
    while days:                     # 리스트(days)의 길이가 0 보다 클때 (= None이 아닐 때까지)
        cnt = 1                     # cnt(배포 가능한 기능 수)를 1로 초기화
        day = days.pop(0)           

        while days:                 
            if day >= days[0]:      
                days.pop(0)         # days에서 day보다 작은 값들을 계속해서 pop
                cnt += 1            # pop 하게 되면 cnt +1
            else:
                break               # days[0]이 day보다 크다면 break
        answer.append(cnt)          

    return answer

print(solution([93,30,55], [1,30,5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))