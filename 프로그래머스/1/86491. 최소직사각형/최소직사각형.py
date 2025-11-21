def solution(sizes):
    answer = 0
    
    # sizes 순회하면서 큰 수를 왼쪽에, 작은 수를 오른쪽에
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
    
    # 큰 수 중에 가장 큰 수, 작은 수 중에 가장 큰 수끼리 곱하기
    sizes.sort(key = lambda x: x[0])
    b_biggest = sizes[-1][0]

    sizes.sort(key = lambda x: x[1])
    s_biggest = sizes[-1][1]
    
    return b_biggest * s_biggest