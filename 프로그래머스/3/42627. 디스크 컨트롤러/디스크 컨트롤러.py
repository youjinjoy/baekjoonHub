import heapq as hq

def solution(jobs):

    
    waiting_list = []
    ready_list = []
    
    for i, job in enumerate(jobs):
        start, duration = job
        waiting_list.append((start, duration, i))
    
    waiting_list.sort(key = lambda x: x[0])

    result = []
    t = 0
    idx = 0
    
    while waiting_list or ready_list:
        
        cnt = 0            
        for s, d, i in waiting_list:
            if s <= t:
                hq.heappush(ready_list, (d, s, i))
                cnt += 1

        if cnt > 0:
            waiting_list = waiting_list[cnt:]
        
        
        if not ready_list:
            t = waiting_list[0][0]
        else:        
            d, s, i = hq.heappop(ready_list)
            t += d
            result.append(t-s)
    
    return sum(result) // len(result)