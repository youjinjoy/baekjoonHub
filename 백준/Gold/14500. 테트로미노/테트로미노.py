import sys
from typing import List


def input():
    return sys.stdin.readline().rstrip()

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    global N, M, board, dx, dy, visited

    N, M = read_list()
    board = [read_list() for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    visited = [[False for _ in range(M)] for _ in range(N)]

    T = [[(0,0), (0,1), (0,2), (1,1)],
        [(0,0), (1,0), (2,0), (1,1)],
        [(0,1), (1,1), (2,1), (1,0)],
        [(1,0), (1,1), (1,2), (0,1)]]

    max_result = 0
    t_max_result = 0
    for i in range(N):
        for j in range(M):
            visited[i][j] = True
            max_result = max(max_result, dfs(i, j, 0, [[i,j]]))
            visited[i][j] = False

            for t_path in T:
                t_result = 0
                valid = True
                for ti, tj in t_path:
                    nti = i + ti
                    ntj = j + tj
                    if nti < 0 or nti >= N or ntj < 0 or ntj >= M:
                        valid = False
                        break
                    t_result += board[nti][ntj]

                if valid:
                    t_max_result = max(t_max_result, t_result)

    return max(max_result, t_max_result)

    
def dfs(x, y, depth, path):

    if depth >= 3:
        result = 0
        for i, j in path:
            result += board[i][j]
        return result
        
    max_result = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if visited[nx][ny]:
            continue
        
        path.append([nx, ny])
        visited[nx][ny] = True
        max_result = max(max_result, dfs(nx, ny, depth + 1, path))
        path.pop()
        visited[nx][ny] = False
    
    return max_result


print(solve())