import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def solve():
    N, M = list(map(int, input().split()))
    MAP = [list(map(int, input())) for _ in range(N)]
    visited = [[False for _ in range(M)]for _ in range (N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([[0, 0, 1]]) # x, y, depth
    visited[0][0] = True

    while (queue):
        cx, cy, depth = queue.popleft()
        if cx == N-1 and cy == M-1:
            print(depth)
            break
        
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and MAP[nx][ny] == 1:
                queue.append([nx, ny, depth+1])
                visited[nx][ny] = True

solve()