from collections import defaultdict, deque

def solution(rectangle, characterX, characterY, itemX, itemY):    
    
    edges = defaultdict(bool)
    inside = defaultdict(bool)
    
    for r in rectangle:
        calc_edges(r, edges)
        calc_inside(r, inside)
    
    # BFS
    # 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수
    visited = [[False for _ in range(51)] for _ in range(51)]

    q = deque([(characterX, characterY, 0)])
    visited[characterX][characterY] = True
    
    d = [(1,0), (0,1), (-1,0), (0,-1)]

    while q:
        cx, cy, cnt = q.popleft()
        
        if cx == itemX and cy == itemY:
            return cnt
        
        for i in range(4):
            nx, ny = cx + d[i][0], cy + d[i][1]
            
            if nx <= 0 or nx > 50 or ny <= 0 or ny > 50 or visited[nx][ny]:
                continue
            
            if not is_on_edge(cx, cy, nx, ny, edges) or is_inside(cx, cy, nx, ny, inside):
                continue
                
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
    

def calc_edges(r, edges):
    x1, y1, x2, y2 = r
    
    for i in range(x1, x2):
        edges[f'{i},{y1},{i+1},{y1}'] = True
        edges[f'{i},{y2},{i+1},{y2}'] = True
        edges[f'{i+1},{y1},{i},{y1}'] = True
        edges[f'{i+1},{y2},{i},{y2}'] = True

    for i in range(y1, y2):
        edges[f'{x1},{i},{x1},{i+1}'] = True
        edges[f'{x2},{i},{x2},{i+1}'] = True
        edges[f'{x1},{i+1},{x1},{i}'] = True
        edges[f'{x2},{i+1},{x2},{i}'] = True

def calc_inside(r, inside):
    x1, y1, x2, y2 = r
    
    for i in range(x1 + 1, x2):
        for j in range(y1, y2):
            inside[f'{i},{j},{i},{j+1}'] = True
            inside[f'{i},{j+1},{i},{j}'] = True
    
    for j in range(y1 + 1, y2):
        for i in range(x1, x2):
            inside[f'{i},{j},{i+1},{j}'] = True
            inside[f'{i+1},{j},{i},{j}'] = True
            
    

def is_on_edge(x1, y1, x2, y2, edges):

    if edges[f'{x1},{y1},{x2},{y2}']:
        return True
    
    return False

def is_inside(x1, y1, x2, y2, inside):
    
    if inside[f'{x1},{y1},{x2},{y2}']:
        return True
    
    return False