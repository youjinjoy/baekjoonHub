def solution(answers):

    p1 = [1, 2, 3, 4, 5]
    p1_size = len(p1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5]
    p2_size = len(p2)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p3_size = len(p3)
    
    p1_count, p2_count, p3_count = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == p1[i % p1_size]:
            p1_count += 1
        if answers[i] == p2[i % p2_size]:
            p2_count += 1
        if answers[i] == p3[i % p3_size]:
            p3_count += 1
    
    result = []
    m = max([p1_count, p2_count, p3_count])
    if m == p1_count:
        result.append(1)
    if m == p2_count:
        result.append(2)
    if m == p3_count:
        result.append(3)
    
    return result