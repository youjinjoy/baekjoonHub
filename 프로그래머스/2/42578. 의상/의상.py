from collections import Counter

def solution(clothes):
    
    C = Counter(t for _,t in clothes)
    
    answer = 1
    for n in C.values():
        answer *= (n + 1)
    answer -= 1

    return answer