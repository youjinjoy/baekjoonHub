import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

a, b = list(map(int, input().split(' ')))

M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = list(map(int, input().split(' ')))
    graph[x].append(y)
    graph[y].append(x)


def bfs(start, visited):
    result = []

    q = deque([(start, 0)])
    visited[start] = True

    while q:
        cur, depth = q.popleft()

        if cur == a:
            result.append(depth)
        if cur == b:
            result.append(depth)

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, depth + 1))
    
    return result

answer = -1
visited = [False] * (N + 1)
for i in range(1, N + 1):
    if not visited[i]:
        result = bfs(i, visited)
        if len(result) == 2:
            answer = result[0] + result[1]

print(answer)