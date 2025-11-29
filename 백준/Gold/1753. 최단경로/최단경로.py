import sys
import heapq as hq

input = sys.stdin.readline

V, E = list(map(int,input().split(' ')))
start = int(input())

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, dist = list(map(int,input().split(' ')))
    graph[u].append((dist, v))

distance = [float('inf') for _ in range(V + 1)]
distance[start] = 0

pq = [(0, start)]
while pq:
    dist, now = hq.heappop(pq)

    if distance[now] < dist:
        continue

    for cost, nxt in graph[now]:
        new_cost = dist + cost

        if new_cost < distance[nxt]:
            distance[nxt] = new_cost
            hq.heappush(pq, (new_cost, nxt))

for c in distance[1:]:
    print('INF' if c == float('inf') else c)