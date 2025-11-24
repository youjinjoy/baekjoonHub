from collections import deque

def solution(maps):
    
    answer = 0

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    n = len(maps)
    m = len(maps[0])
    

    queue = deque([(0, 0, 1)])
    maps[0][0] = 0
    
    while queue:
        x, y, c = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return c
        
        for i in range(4):        
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or maps[nx][ny] == 0:
                continue
            
            maps[nx][ny] = 0
            queue.append((nx, ny, c + 1))
    
    return -1