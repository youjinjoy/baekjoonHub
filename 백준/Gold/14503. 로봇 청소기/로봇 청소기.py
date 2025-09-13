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
    global N, M
    N, M = read_list()

    global r, c, d
    r, c, d = read_list()

    # 북, 동, 남, 서
    global dx, dy
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    global room
    room = [read_list() for _ in range(N)]

    queue = deque([[r,c]])
    room[r][c] = 2
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        if should_clean_near(x,y):
            d = (d-1)%4 # 반시계 회전
            nx = x + dx[d]
            ny = y + dy[d]
            while not enable_clean(nx, ny):
                d = (d-1)%4 # 반시계 회전
                nx = x + dx[d]
                ny = y + dy[d]
            queue.append([nx, ny])
            room[nx][ny] = 2
            count += 1
        else:
            nx = x-dx[d]
            ny = y-dy[d]
            if enable_go(nx, ny):
                queue.append([nx, ny])
                room[nx][ny] = 2
            else:
                return count
    return count

def should_clean_near(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 and nx >= N and ny < 0 and ny >= M:
            continue
        if room[nx][ny] == 0:
            return True
    return False

def enable_go(x,y):
    if x < 0 and x >= N and y < 0 and y >= M:
        return False
    if room[x][y] == 1:
        return False
    return True

def enable_clean(x,y):
    if x < 0 and x >= N and y < 0 and y >= M:
        return False
    if room[x][y] == 0:
        return True
    return False


print(solve())