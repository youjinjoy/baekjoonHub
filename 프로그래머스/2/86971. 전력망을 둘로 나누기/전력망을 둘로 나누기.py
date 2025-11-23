from collections import deque

def solution(n, wires):
    
    # 전선 하나 끊기
    # 해당 전선 상태에서 각 네트워크 개수 세기
    # -> 네트워크 개수 비교해 최솟값 저장
    
    min_count = 100
    
    for i in range(n - 1):
        new_wires = wires[:i] + wires[i+1:]
        
        
        graph = [[] for _ in range(n + 1)]
        
        for a, b in new_wires:
            graph[a].append(b)
            graph[b].append(a)
            
        min_count = min(min_count, count_nodes(n, graph))
        
    return min_count

def count_nodes(n, graph):
    
    visited = [False for _ in range(n + 1)]
    
    result = []
    
    for i in range(1, n + 1):
        count = bfs(n, i, graph, visited)
        if count > 0:
            result.append(count)
    return result[1] - result[0] if result[1] >= result[0] else result[0] - result[1]
    
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
            