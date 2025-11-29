import sys
import heapq as hq

input = sys.stdin.readline

N, M, X = list(map(int, input().split(' ')))

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, dest, cost = list(map(int, input().split(' ')))
    graph[start].append((cost, dest))
    reverse_graph[dest].append((cost, start))

def dijkstra(graph):
    distance = [float('inf') for _ in range(N + 1)]

    distance[X] = 0
    pq = [(0, X)]

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

to_X = dijkstra(graph)
from_X = dijkstra(reverse_graph)

ans = 0
for i in range(1, N + 1):
    ans = max(ans, to_X[i] + from_X[i])

print(ans)