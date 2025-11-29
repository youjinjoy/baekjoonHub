import sys
import heapq as hq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, dest, cost = list(map(int, input().split(' ')))
    graph[start].append((cost, dest))

start, dest = list(map(int, input().split(' ')))

distance = [float('inf') for _ in range(n + 1)]
distance[start] = 0

prev = [-1] * (n + 1)

pq = [(0, start)]

while pq:
    dist, now = hq.heappop(pq)

    if distance[now] < dist:
        continue

    for cost, nxt in graph[now]:
        new_dist = dist + cost
        if new_dist < distance[nxt]:
            prev[nxt] = now
            distance[nxt] = new_dist
            hq.heappush(pq, (new_dist, nxt))
    

print(distance[dest])

path = []
cur = dest

while cur != -1:
    path.append(cur)
    cur = prev[cur]

path.reverse()

print(len(path))
print(*path)