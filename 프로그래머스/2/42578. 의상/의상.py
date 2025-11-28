from collections import defaultdict

def solution(clothes):
    D = defaultdict(int)
    for c, t in clothes:
        D[t] += 1
    
    
    answer = 1
    for n in D:
        answer *= (D[n] + 1)
    answer -= 1

    return answer