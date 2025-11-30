def solution(citations):
    answer = 0

    citations.sort()
    n = len(citations)
    
    h = 0
    for i in range(len(citations)):
        if citations[i] >= n - i:
            return n - i
            
    return h