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
    N, M, X = read_list()

    adj = [[] for _ in range(N + 1)]    
    for _ in range(M):
        a, b, time = read_list()
        adj[a].append((time, b))
    
    INF = float('inf')

    def dijkstra(start):
        times = [INF for _ in range(N + 1)]
        heap = [(0, start)]
        times[start] = 0

        while heap:
            ct, u = hq.heappop(heap)

            if times[u] < ct:
                continue

            for nt, v in adj[u]:
                time = ct + nt
                if ct + nt < times[v]:
                    hq.heappush(heap, (time, v))
                    times[v] = time

        return times
    
    going_times = [dijkstra(i)[X] for i in range(N+1)]
    coming_times = dijkstra(X)

    answer = 0
    for j in range(1, N+1):
        answer = max(answer, going_times[j] + coming_times[j])

    print(answer)

solve()