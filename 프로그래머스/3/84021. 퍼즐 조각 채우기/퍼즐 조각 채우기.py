from collections import deque, defaultdict

def solution(game_board, table):
    
    # game_board 내 도형 추출
    space_arr = calc_shape_map(game_board, 0)
    
    # table 내 도형 추출
    figure_arr = calc_shape_map(table, 1)

    result = []
    visited_space = [False for _ in range(len(space_arr))]
    visited_figure = [False for _ in range(len(figure_arr))]
    for j in range(len(space_arr)):
        s = space_arr[j]
        for i in range(len(figure_arr)):
            f = figure_arr[i]
            rf = rotate_cw(f)
            rrf = rotate_cw(rf)
            rrrf = rotate_cw(rrf)
            rotated = [f, rf, rrf, rrrf]
            for r in rotated:
                if not visited_space[j] and not visited_figure[i] and is_fit(s, r):
                    visited_space[j] = True
                    visited_figure[i] = True
                    result.append(f)
                    break
    
    answer = 0

    for figure in result:
        for i in range(len(figure)):
            for j in range(len(figure[0])):
                if figure[i][j] == 1:
                    answer += 1
                
    return answer


def is_fit(space, figure):
    sh, sw = len(space), len(space[0])
    fh, fw = len(figure), len(figure[0])
    
    if sh != fh or sw != fw:
        return False
    
    for i in range(sh):
        for j in range(sw):
            if space[i][j] != figure[i][j]:
                return False
    
    return True

# 회전 함수 (시계 방향)
def rotate_cw(figure):
    w, h = len(figure[0]), len(figure)
    
    new_figure = [[-1 for _ in range(h)] for _ in range(w)]
    
    for j in range(w):
        for i in range(h):
            new_figure[j][i] = figure[h-i-1][j]
    
    return new_figure

def calc_shape_map(maps, target):
    w, h = len(maps[0]), len(maps)
    visited = [[False for _ in range(w)] for _ in range(h)]
    shape_map = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] == target:
                coords = bfs(i, j, target, maps, visited, shape_map)
                if len(coords):
                    shape = coords_to_maps(coords)
                    shape_map.append(shape)
    
    return shape_map

def bfs(start_x, start_y, target, maps, visited, result):
    
    w, h = len(maps[0]), len(maps)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    shape = []
    
    while q:
        cx, cy = q.popleft()
        shape.append((cx, cy))
        
        for i in range(4):
            nx, ny = cx + d[i][0], cy + d[i][1]
            
            if nx < 0 or nx >= h or ny < 0 or ny >= w or visited[nx][ny]:
                continue
            
            if maps[nx][ny] != target:
                continue
            
            visited[nx][ny] = True
            q.append((nx, ny))
    
    return shape

def coords_to_maps(coords):

    max_x, max_y = 0, 0
    min_x, min_y = float('inf'), float('inf')

    for i in range(len(coords)):
        
        min_x = min(min_x, coords[i][0])
        max_x = max(max_x, coords[i][0])

        min_y = min(min_y, coords[i][1])       
        max_y = max(max_y, coords[i][1])
        
    w = max_y - min_y + 1
    h = max_x - min_x + 1

    maps = [[0 for _ in range(w)] for _ in range(h)]
    
    for i in range(len(coords)):
        x, y = coords[i][0] - min_x, coords[i][1] - min_y
        maps[x][y] = 1
    
    return maps