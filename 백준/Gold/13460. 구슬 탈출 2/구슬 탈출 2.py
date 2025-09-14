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

    global board
    board = [list(input()) for _ in range(N)]

    
    R = (-1, -1)
    B = (-1, -1)

    global O, X
    O = (-1, -1)
    X = (-1, -1)

    visited = set()
    visited.add((R, B)) # 무효 처리로 사용

    for i in range(1,N):
        for j in range(1,M):
            if board[i][j] == 'R':
                R = (i,j)
            if board[i][j] == 'B':
                B = (i,j)
            if board[i][j] == 'O':
                O = (i,j)

    global dx, dy
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(R, B, 0)])
    visited.add((R, B))
    count = 1

    while queue:
        r, b, count = queue.popleft()

        if r == O:
            return count

        if count >= 10:
            return -1
        
        for i in range(4):
            nr, nb = get_next_position(r, b, i)
            if (nr, nb) in visited:
                continue

            if nb == O:
                continue
            
            if nr == O:
                return count + 1

            queue.append((nr, nb, count + 1))
            visited.add((nr, nb))

    return -1

def get_next_position(r, b, d): # direction
    rx, ry = r
    bx, by = b

    state = get_state(r,b)

    if d == 0:
        if state == 'red-up':
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, (rx, ry), d)
        elif state == 'red-bottom':
            bx, by = move_to_end(bx, by, X, d)
            rx, ry = move_to_end(rx, ry, (bx, by), d)
        else:
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, X, d)
    elif d == 1:
        if state == 'red-up':
            bx, by = move_to_end(bx, by, X, d)
            rx, ry = move_to_end(rx, ry, (bx, by), d)
        elif state == 'red-bottom':
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, (rx, ry), d)
        else:
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, X, d)
    elif d == 2:
        if state == 'red-right':
            bx, by = move_to_end(bx, by, X, d)
            rx, ry = move_to_end(rx, ry, (bx, by), d)
        elif state == 'red-left':
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, (rx, ry), d)
        else:
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, X, d)
    else:
        if state == 'red-right':
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, (rx, ry), d)
        elif state == 'red-left':
            bx, by = move_to_end(bx, by, X, d)
            rx, ry = move_to_end(rx, ry, (bx, by), d)
        else:
            rx, ry = move_to_end(rx, ry, X, d)
            bx, by = move_to_end(bx, by, X, d)

    return ((rx, ry), (bx, by))


def move_to_end(x, y, rb, d):

    nx = x + dx[d]
    ny = y + dy[d]

    while board[nx][ny] != '#':  # 사방이 벽이기 때문에 경계값 검사 안해도 됨

        if board[nx][ny] == 'O':
            return (nx, ny)
        
        if (nx, ny) == rb:
            return (x, y)

        x, y = nx, ny
        nx += dx[d]
        ny += dy[d]
    
    return (x, y)

def get_state(r, b):
    rx, ry = r
    bx, by = b

    if rx == bx:    # 수평 방향
        if ry > by: # red가 blue 보다 오른쪽
            return 'red-right'
        else:
            return 'red-left'

    if ry == by:    # 수직 방향
        if rx > bx: # red가 blue 보다 아래쪽
            return 'red-bottom'
        else:
            return 'red-up'
    
    return 'not-same-line'


print(solve())