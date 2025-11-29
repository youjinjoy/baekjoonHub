import sys
import heapq as hq

input = sys.stdin.readline

N, M, X = list(map(int, input().split(' ')))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, dest, cost = list(map(int, input().split(' ')))
    graph[start].append((cost, dest))


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

result = dijkstra(X)

for i in range(1, N + 1):

    result[i] += dijkstra(i)[X]

print(max(result[1:]))