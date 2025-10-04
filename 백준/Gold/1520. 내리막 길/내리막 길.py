import sys
sys.setrecursionlimit(10**6)
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    N, M = read_list()

    MAP = [read_list() for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

        
    def dfs(x, y):
        
        if x == N - 1 and y == M - 1:
            return 1

        if dp[x][y] != -1:
            return dp[x][y]

        dp[x][y] = 0
        for i in range(4):
            
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if MAP[x][y] <= MAP[nx][ny]:
                continue
            
            dp[x][y] += dfs(nx, ny)
        
        return dp[x][y]
        
    return dfs(0, 0)

print(solve())