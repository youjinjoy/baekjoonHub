from collections import defaultdict

def solution(genres, plays):
    
    # 총 재생 수 내림차순으로 정렬된 장르
    S = set(genres)
    genre_order = list(S)
    
    
    # 장르 키 - (재생 수 내림차순, 고유 번호 오름차순)으로 정렬된 고유 번호 배열
    G = defaultdict(list)
    
    
    #
    N = len(genres)
    total_plays = defaultdict(int)
    for i in range(N):
        G[genres[i]].append(i)
        total_plays[genres[i]] += plays[i]
    
    #
    genre_order.sort(key = lambda g: total_plays[g], reverse = True)

    #
    for g in genre_order:
        G[g].sort(key = lambda i: (-plays[i], i))
    
    #
    answer = []
    for g in genre_order:
        cnt = 0
        for music_num in G[g]:
            answer.append(music_num)
            cnt += 1
            if cnt >= 2:
                break
    
    return answer