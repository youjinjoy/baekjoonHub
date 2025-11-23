def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if ((yellow // i) + i) * 2 + 4 == brown:
                answer = [yellow // i + 2, i + 2]
                break

    return answer