from collections import defaultdict

def solution(genres, plays):
    
    # 장르 키 - (재생 수 내림차순, 고유 번호 오름차순)으로 정렬된 고유 번호 / 개별 재생 수 배열
    G = defaultdict(list)
    # 장르 키 - 총 재생 수
    total_plays = defaultdict(int)

    for i in range(len(genres)):
        G[genres[i]].append((i, plays[i]))
        total_plays[genres[i]] += plays[i]

    # 총 재생 수 내림차순으로 정렬된 장르
    genre_order = sorted(total_plays.keys(), key = lambda g: total_plays[g], reverse = True)

    answer = []
    for g in genre_order:
        sorted_g = sorted(G[g], key = lambda x: (-x[1], x[0]))
        answer.extend(num for num, _ in sorted_g[:2])
                            
    return answer