import heapq as hq
from collections import defaultdict

def solution(operations):
    
    min_q = []
    max_q = []
    deleted = defaultdict(bool)
    idx = 0
    
    for op in operations:
        c, n = op.split(' ')
        n = int(n)
        
        if c == 'I':
            hq.heappush(max_q, (-n, idx))
            hq.heappush(min_q, (n, idx))
            idx += 1
            
        elif c == 'D' and n == 1 and max_q:
            
            top = max_q[0]
            c_n, c_idx = top
            
            while max_q and deleted[c_idx]:
                deleted[c_idx] = False
                _, c_idx = hq.heappop(max_q)
            
            if max_q:
                d = hq.heappop(max_q)
                deleted[d[1]] = True
            
        elif c == 'D' and n == -1 and min_q:
            
            top = min_q[0]
            c_n, c_idx = top
            
            while min_q and deleted[c_idx]:
                deleted[c_idx] = False
                _, c_idx = hq.heappop(min_q)
            
            if min_q:
                d = hq.heappop(min_q)
                deleted[d[1]] = True

    max_top = 0
    min_top = 0
    while max_q:
        if deleted[max_q[0][1]]:
            hq.heappop(max_q)
        else:
            max_top = -max_q[0][0]
            break
    
    while min_q:
        if deleted[min_q[0][1]]:
            hq.heappop(min_q)
        else:
            min_top = min_q[0][0]
            break
    
    return [max_top, min_top]
