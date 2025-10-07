def solution(m, n, board):
    erased = 0
    
    board = [list(row) for row in board]
    
    while True:
        erased_all = True
        coordinates = []
        for i in range(m):
            for j in range(n):
                if board[i][j] != '@' and is_erasable(i, j, m, n, board):
                    coordinates.append((i, j))
                    erased_all = False
                    
        if erased_all:
            break
            
        for i, j in coordinates:
            erase(i, j, board)
        erased = fall_blocks(m, n, board)

    return erased

def is_erasable(x, y, m, n, board):
    
    if board[x][y].islower():
        return False
        
    D = [[0, 1], [1, 0], [1, 1]]
    
    for dx, dy in D:

        nx, ny = x + dx, y + dy

        if nx >= m or ny >= n:
            return False
        
        if board[nx][ny] != board[x][y]:
            return False
    
    return True

def erase(x, y, board):
    D = [[0, 0], [0, 1], [1, 0], [1, 1]]
    
    for dx, dy in D:
        nx, ny = x + dx, y + dy
        
        board[nx][ny] = '@'

def fall_blocks(m, n, board):
    
    x_total_count = 0

    for j in range(n):
        result = []
        
        for i in range(m):
            if board[m-i-1][j] != '@':
                result.append(board[m-i-1][j])

        result.reverse()        
        x_count = m - len(result)
        x_total_count += x_count
        
        if x_count == 0:
            continue
            
        for i in range(x_count):
            board[i][j] = '@'
        for i in range(x_count, m):
            board[i][j] = result[i - x_count]
            
    return x_total_count