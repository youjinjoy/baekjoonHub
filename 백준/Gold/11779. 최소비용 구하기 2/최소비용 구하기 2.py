import sys
from typing import List
import heapq as hq


def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    n = read_int()
    m = read_int()

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, cost = read_list()
        adj[a].append((cost, b))

    INF = float('inf')
    distance = [INF for _ in range(n + 1)]
    prev = [-1 for _ in range(n + 1)]

    start, end = read_list()
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        c, u = hq.heappop(heap)

        if c > distance[u]:
            continue

        for w, v in adj[u]:
            nc = c + w
            if nc < distance[v]:
                hq.heappush(heap, (nc, v))
                distance[v] = nc
                prev[v] = u
    
    print(distance[end])
    
    node = end
    result = [end]
    count = 1
    while node != start:
        node = prev[node]
        result.append(node)
        count += 1
    print(count)

    result.reverse()
    print(*result)
    
solve()