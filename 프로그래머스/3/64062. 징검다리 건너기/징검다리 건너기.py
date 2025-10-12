def solution(stones, k):
    answer = 0

    # stones 배열 순회하면서 -n (이분 탐색)
    # 동시에 0 이하 되는 것의 연속 구간이 k개 이상 되는 부분을 찾는다.
    start, end = 1, 200_000_000

    while start <= end:
        mid = (start + end) // 2
        # print('s', start, 'e', end, 'm', mid)
        
        section = 0
        can_cross = True
        for stone in stones:
            if stone - mid < 0:
                section += 1
                if section >= k:
                    can_cross = False
                    break
            else:
                section = 0
        
        if can_cross:
            start = mid + 1
        else:
            end = mid - 1

    return end