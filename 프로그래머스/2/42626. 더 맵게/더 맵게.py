import heapq as hq

def solution(scoville, K):
    cnt = 0
    
    hq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        a = hq.heappop(scoville)
        b = hq.heappop(scoville)
        hq.heappush(scoville, a + b * 2)
        cnt += 1
    
    if len(scoville) == 0:
        return -1
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    
    return cnt