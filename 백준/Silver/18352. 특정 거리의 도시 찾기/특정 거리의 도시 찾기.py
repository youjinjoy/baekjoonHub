import sys
from typing import List
import heapq as hq

def input():
    return sys.stdin.readline().rstrip()

def read_list() -> List[int]:
    return list(map(int, input().split()))

def solve():
    N, M, K, X = read_list()

    adj = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = read_list()
        adj[a].append(b)

    INF = float('inf')
    distance = [INF for _ in range(N + 1)]

    distance[X] = 0
    heap = [(0, X)]

    while heap:

        d, node = hq.heappop(heap)
        if d > distance[node]:
            continue
        
        for next_node in adj[node]:
            next_distance = d + 1
            if next_distance < distance[next_node]:
                distance[next_node] = next_distance
                hq.heappush(heap, (next_distance, next_node))
        
    
    flag = False
    for index, d in enumerate(distance):
        if d == K:
            print(index)
            flag = True

    if not flag:
        print(-1)

solve()