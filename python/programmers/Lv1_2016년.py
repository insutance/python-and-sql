def solution(a, b):
    month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    days = 0
    if a == 1:
        day = b % 7
    else:
        for i in range(a-1):
            days += month_day[i]
        day = (days + b) % 7
    
    if day == 0:
        answer = 'THU'
    elif day == 1:
        answer = 'FRI'
    elif day == 2:
        answer = 'SAT'
    elif day == 3:
        answer = 'SUN'
    elif day == 4:
        answer = 'MON'
    elif day == 5:
        answer = 'TUE'
    elif day == 6:
        answer = 'WED'
    
    return answer

print(solution(1,31))
