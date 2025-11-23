def solution(n, computers):
    
    visited = [False for _ in range(n)]
    
    answer = 0

    for start in range(n):
        if not visited[start]:
            dfs(start, computers, visited)
            answer += 1
        
    return answer

def dfs(cur, computers, visited):
    
    visited[cur] = True
    
    for nxt in range(len(computers)):
        
        if cur != nxt and computers[cur][nxt] and not visited[nxt]:
            dfs(nxt, computers, visited)
