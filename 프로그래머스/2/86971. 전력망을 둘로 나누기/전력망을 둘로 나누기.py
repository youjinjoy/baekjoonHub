from collections import deque

def solution(n, wires):
    
    min_sub = 100
    
    # 전선 하나 끊기
    for i in range(n - 1):
        new_wires = wires[:i] + wires[i+1:]
        
        graph = [[] for _ in range(n + 1)]
        
        for a, b in new_wires:
            graph[a].append(b)
            graph[b].append(a)
            
        # 해당 전선 상태에서 각 네트워크 개수 세기
        count = get_count(n, graph)

        # 네트워크 개수 비교해 최솟값 저장
        min_sub = min(min_sub, abs((n - count) - count))
        
    return min_sub

def get_count(n, graph):
    
    visited = [False for _ in range(n + 1)]
    
    count = bfs(n, 1, graph, visited)
    if count > 0:
        return count
    
def bfs(n, start, graph, visited):
    
    if visited[start]:
        return 0
    
    queue = deque([start])
    visited[start] = True
    count = 1
    
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)
                count += 1
    
    return count
            