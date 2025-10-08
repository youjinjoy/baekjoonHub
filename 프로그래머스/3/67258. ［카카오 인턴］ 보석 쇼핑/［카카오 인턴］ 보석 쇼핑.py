def solution(gems):
    answer = []
    shortest = float('inf')

    p1, p2 = 0, 0
    gems_set = set(gems)
    gems_counted = {}
    
    for p2 in range(len(gems)):
        gems_counted[gems[p2]] = gems_counted.get(gems[p2], 0) + 1

        # 모든 종류의 보석을 포함할 때까지 p2 이동
        if len(gems_counted) == len(gems_set):
            # 모든 종류의 보석을 포함하는 최소 구간을 구할 때까지 p1 이동
            while p1 <= p2:
                if gems_counted.get(gems[p1]) == 1:
                    if p2 - p1 < shortest:
                        shortest = p2 - p1
                        answer = [p1 + 1, p2 + 1]
                    break
                gems_counted[gems[p1]] -= 1
                if gems_counted[gems[p1]] == 0:
                    del gems_set[gems[p1]]
                p1 += 1
            

        # p2에서 한 칸 이동
        p2 += 1
        # 모든 종류의 보석을 포함하는 최소 구간을 구할 때까지 p1 이동 -> 순회
        # p2가 끝에 다다르고, 마지막으로 p1 이동할 때까지 반복 -> 순회
        
    return answer