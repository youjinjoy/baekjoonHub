from collections import deque

def solution(maps):
    
    answer = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(maps)
    m = len(maps[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return c
        
        for i in range(4):        
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
                
            if maps[nx][ny] == 0:
                continue
            
            visited[nx][ny] = True
            queue.append((nx, ny, c + 1))
    
    return -1