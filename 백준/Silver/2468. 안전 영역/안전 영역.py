import sys
from typing import List

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():

    global N, area, d

    N = read_int()

    area = [read_list() for _ in range(N)]

    k_set = set()
    k_set.add(0)

    for row in area:
        for j in row:
            k_set.add(j)

    d = [(1,0), (0,1), (0, -1), (-1, 0)]


    max_count = 0
    k_list = list(k_set)
    for k in k_list:
        count = 0
        global visited
        visited = [[False for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j] and area[i][j] > k:
                    count += dfs(i, j, k)
        max_count = max(max_count, count)

    print(max_count)

def dfs(x,y,k):
    
    visited[x][y] = True
    
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue

        if visited[nx][ny]:
            continue

        if area[nx][ny] <= k:
            continue

        dfs(nx, ny, k)
    
    return 1


solve()