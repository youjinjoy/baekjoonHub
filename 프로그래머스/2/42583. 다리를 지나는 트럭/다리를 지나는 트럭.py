from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    trucks = deque(truck_weights)
    bridges = deque([0 for _ in range(bridge_length)])
    t = 0
    w = 0

    while trucks or w != 0:
        t += 1

        popped = bridges.popleft()
        w -= popped
        
        if trucks and w + trucks[0] <= weight:
            cw = trucks.popleft()
            w += cw
            bridges.append(cw)
        else:
            bridges.append(0)
        
    
    return t