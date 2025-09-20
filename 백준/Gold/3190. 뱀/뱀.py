import sys
from collections import deque
input=sys.stdin.readline

n=int(input()) # 보드의 크기
# 보드 초기화 (0번 인덱스는 사용하지 않는다.)
board = [[0] * (n+1) for _ in range(n+1)]

k=int(input()) # 사과의 개수
# 사과의 위치
for _ in range(k):
    a,b=list(map(int,input().strip().split(' ')))
    board[a][b] = 1

l=int(input()) # 뱀의 방향 변환 횟수
directions={}
# 뱀의 방향 변환
for _ in range(l):
    x,c=list(input().strip().split(' '))
    directions[int(x)]=c

# 뱀의 현재 방향 (상, 우, 하, 좌)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
direction = 1  # 시작 방향은 오른쪽. !!! dx, dy 1번 인덱스 보기 !!!


snake = [(1, 1)]  # 뱀의 초기 위치
time = 0

while True:
    time += 1
    head = snake[-1]
    nx, ny = head[0] + dx[direction], head[1] + dy[direction]
    
    # 벽이나 자신의 몸에 부딪히면 종료
    if nx <= 0 or nx > n or ny <= 0 or ny > n or (nx, ny) in snake:
        break

    # 사과가 있다면(board 값 1) 먹고 꼬리는 그대로, 없다면 꼬리를 줄임
    if board[nx][ny] == 1:
        board[nx][ny] = 0 # (먹어서 board 값 0)
    else:
        snake.pop(0)
    snake.append((nx, ny))

    # 방향 전환
    if time in directions:
        if directions[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

print(time)