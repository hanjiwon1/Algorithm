def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = [0]*bridge_length
    sec = 0

    while True:
        if len(truck_weights) != 0:
            bridge_queue.pop(0)
            bridge_queue.append(0)
            bridge_queue[len(bridge_queue)-1] = 0
            sec += 1
            if sum(bridge_queue) + truck_weights[0] <= weight:
                bridge_queue[len(bridge_queue)-1] = truck_weights[0]
                # print(bridge_queue)
                del truck_weights[0]

        else:
            sec += len(bridge_queue)
            break
    answer = sec
    return answer


bridge_length = int(input())
weight = int(input())
truck_weights = list(map(int, input().split()))
print(solution(bridge_length, weight, truck_weights))
