"""백준-회의실배정"""
#1. 시작 시간 기준으로 정렬을 한 후, 다시 종료 시간 기준으로 정렬을 한다.
#2. 그 후, 종료 시간과 다음 시작 시간을 비교한다.

n = int(input())

met_info = []
for i in range(n):
    met_info.append(list(map(int, input().split())))

met_info = sorted(met_info, key=lambda info: info[0])
met_info = sorted(met_info, key=lambda info: info[1])

meeting_count = 0
start = 0

for meeting in met_info:
    if meeting[0] >= start:
        start = meeting[1]
        meeting_count += 1

print(meeting_count)