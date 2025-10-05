import sys
from typing import List
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

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
    queue = deque([X])

    while queue:
        u = queue.popleft()

        for w in adj[u]:
            if distance[u] + 1 < distance[w]:
                distance[w] = distance[u] + 1
                queue.append(w)


    result = [index for index, d in enumerate(distance) if d == K]

    if result:
        print('\n'.join(map(str, result)))
    else:
        print(-1)

solve()