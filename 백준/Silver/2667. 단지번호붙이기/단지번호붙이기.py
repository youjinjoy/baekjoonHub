import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

maps = [list(map(int, input().strip())) for _ in range(N)]

visited = [[False] * N for _ in range(N)]

def bfs(x, y):
    q = deque([(x, y)])
    maps[x][y] = 2
    cnt = 0

    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        cx, cy = q.popleft()
        cnt += 1

        for i in range(4):
            nx, ny = cx + d[i][0], cy + d[i][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or maps[nx][ny] != 1:
                continue

            visited[nx][ny] = True
            maps[nx][ny] = 2
            q.append((nx, ny))
    
    return cnt

result = []
for i in range(N):
    for j in range(N):
        if not visited[i][j] and maps[i][j] == 1:
            result.append(bfs(i, j))

print(len(result))

result.sort()
for cnt in result:
    print(cnt)