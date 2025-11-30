import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = list(map(int, input().split(' ')))
    graph[a].append(b)
    graph[b].append(a)


def dfs(cur, visited):
    visited[cur] = True
    
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt, visited)
    

visited = [False] * (N + 1)
dfs(1, visited)
print(sum(visited) - 1)