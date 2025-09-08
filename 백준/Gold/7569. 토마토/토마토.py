import sys
from typing import List
from collections import deque


def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():

    M, N, H = read_list()
    box = [[read_list() for _ in range(N)] for _ in range(H)]
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
    # box[1][1][2]: 1
    # Z,X,Y

    dx = [1, 0, 0, -1, 0, 0]
    dy = [0, 1, 0, 0, -1, 0]
    dz = [0, 0, 1, 0, 0, -1]

    queue = deque([])
    count = 0

    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y] == 1:
                    queue.append([x, y, z, 0])
                    visited[z][x][y] = True

    while queue:
        cx, cy, cz, day = queue.popleft()
        count = day

        for i in range(6):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nz = cz + dz[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue

            if visited[nz][nx][ny] or box[nz][nx][ny] == -1:
                continue

            if box[nz][nx][ny] == 0:
                queue.append([nx, ny, nz, day+1])
                visited[nz][nx][ny] = True
                box[nz][nx][ny] = 1
        
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y] == 0:
                    return -1
    
    return count
    
print(solve())