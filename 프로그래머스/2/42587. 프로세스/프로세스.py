from collections import deque

def solution(priorities, location):
    
    q = deque([(p, i) for i, p in enumerate(priorities)])

    order = 1
    while q:
        p, i = q.popleft()
        
        bigger_exist = False
        for j in range(len(q)):
            if p < q[j][0]:
                bigger_exist = True
                break
        
        if bigger_exist:
            q.append((p, i))
            continue
        
        if location == i:
            return order
        
        order += 1