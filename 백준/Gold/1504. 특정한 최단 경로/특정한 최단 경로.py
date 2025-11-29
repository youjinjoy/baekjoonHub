import sys
import heapq as hq
input = sys.stdin.readline

N, M = list(map(int, input().split(' ')))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, dest, cost = list(map(int, input().split(' ')))
    graph[start].append((cost, dest))
    graph[dest].append((cost, start))

v1, v2 = list(map(int, input().split(' ')))

def dijkstra(start):

    distance = [float('inf') for _ in range(N + 1)]
    distance[start] = 0

    pq = [(0, start)]

    while pq:
        dist, cur = hq.heappop(pq)

        if distance[cur] < dist:
            continue

        for cost, nxt in graph[cur]:
            new_dist = dist + cost
            if new_dist < distance[nxt]:
                distance[nxt] = new_dist
                hq.heappush(pq, (new_dist, nxt))
    
    return distance
    
from_start = dijkstra(1)
from_v1 = dijkstra(v1)
from_v2 = dijkstra(v2)

a = from_start[v1] + from_v1[v2] + from_v2[N]
b = from_start[v2] + from_v2[v1] + from_v1[N]

if a == float('inf') and b == float('inf'):
    print(-1)
elif a == float('inf'):
    print(b)
elif b == float('inf'):
    print(a)
else:
    print(min(a, b))