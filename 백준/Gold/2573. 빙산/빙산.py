import sys
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():

    global N, M
    N, M = read_list()

    global dx, dy
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    original_map = [read_list() for _ in range(N)]

    current_map = original_map
    year = 0
    while not is_separated(current_map):
        if is_all_melted(current_map):
            return 0

        current_map = get_map_after_one_year(current_map)
        year += 1
    
    return year

 
def get_map_after_one_year(original_map):
    new_map = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(1,N-1):
        for j in range(1,M-1):
            cur = original_map[i][j]
            if cur > 0:
                melt = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if original_map[ni][nj] == 0:
                        melt += 1
                new_map[i][j] = max(0, cur - melt)

    return new_map

def is_separated(current_map):
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0

    for i in range(1, N-1):
        for j in range(1, M-1):

            if not visited[i][j] and current_map[i][j] > 0:
                stack = [[i,j]]
                visited[i][j] = True

                while stack:
                    [x, y] = stack.pop()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if not visited[nx][ny] and current_map[nx][ny] > 0:
                            stack.append([nx,ny])
                            visited[nx][ny] = True

                count += 1

    return count >= 2

def is_all_melted(current_map):
    
    for i in range(1,N-1):
        for j in range(1,M-1):
            if current_map[i][j] > 0:
                return False
    
    return True

print(solve())