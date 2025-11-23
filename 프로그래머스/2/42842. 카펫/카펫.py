
def solution(brown, yellow):
    
    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h
            
            if (w + h) * 2 + 4 == brown:
                return [w + 2, h + 2]