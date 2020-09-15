def solution(bridge_length, weight, truck_weights):
    Q = [0] * bridge_length
    cur_truck = 0
    time = 0
    while cur_truck != len(truck_weights):
        time+=1
        Q.pop(0)
        if sum(Q) + truck_weights[cur_truck] <= weight:
            Q.append(truck_weights[cur_truck])
            cur_truck+=1
        else:
            Q.append(0)
    return time+bridge_length


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
# truck_weights = [10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)