def solution(bridge_length, weight, truck_weights):
    crossingTrucks = []     # 지나가고 있는 트럭 리스트
    out_times = []          # 나가는 시간 리스트

    time = 0
    while True:
        if crossingTrucks == [] and truck_weights == []:            # 둘 다 빈 배열이면 다 지나감
            break

        if out_times:
            if out_times[0] == time:                                # 나가는 시간 배열이 time(현재시간)과 같다면
                crossingTrucks.pop(0)                               # 지나가는 트럭 리스트 pop
                out_times.pop(0)                                    

        if truck_weights:
            if sum(crossingTrucks) + truck_weights[0] <= weight:    # 트럭의 무게가 최대 무게보다 작을 때만 추가
                crossingTrucks.append(truck_weights.pop(0))         # truch_weights 에서 pop
                out_times.append(time + bridge_length)              # out_times에 (시간+다리 길이) 한 값을 추가
        
        time += 1       # 시간은 계속해서 가고 있으므로 +1

    return time

print(solution2(2, 10, [7,4,5,6]))
print(solution2(100,100, [10]))
print(solution2(100,100, [10,10,10,10,10,10,10,10,10,10]))
