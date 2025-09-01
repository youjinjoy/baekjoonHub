import sys
from collections import deque

input = sys.stdin.readline

def solve():
    N, M, V = list(map(int, input().split(' ')))
    
    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        a, b =  list(map(int, input().split(' ')))
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    for adj in graph:
        graph[adj].sort()

        
    visited = set()
    dfs_path = []
    def dfs(cur):
        if cur in visited:
            return
        
        visited.add(cur)
        dfs_path.append(cur)

        for next in graph[cur]:
            dfs(next)

    dfs(V)

    
    visited = set()
    bfs_path = []
    visited.add(V)
    queue = deque([V])
    def bfs():

        while (queue):
            cur = queue.popleft()
            bfs_path.append(cur)
            
    
            for next in graph[cur]:
                if not next in visited:
                    visited.add(next)
                    queue.append(next)

    bfs()

    print(*dfs_path)
    print(*bfs_path)

solve()
