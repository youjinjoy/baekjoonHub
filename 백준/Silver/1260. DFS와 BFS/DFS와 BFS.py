import sys
from collections import deque
input = sys.stdin.readline

N, M, V = list(map(int, input().split(' ')))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = list(map(int, input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort()

def dfs(cur, visited, result):
    visited[cur] = True
    result.append(cur)

    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt, visited, result)

def bfs(start, visited, result):
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

visited = [False for _ in range(N + 1)]
result = []
dfs(V, visited, result)
print(*result)

visited = [False for _ in range(N + 1)]
result = []
bfs(V, visited, result)
print(*result)

