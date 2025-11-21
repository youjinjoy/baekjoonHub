def solution(sizes):
    
    max_w, max_h = 0, 0
    for a, b in sizes:
        # 가로 길이가 항상 세로 길이보다 크도록
        w, h = max(a, b), min(a, b)
        # 순회하면서 가로, 세로 최대값 구하기
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        
    return max_w * max_h