import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
visited = [False for _ in range(N + 1)]
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs()

            visited[i] = False
            result.pop()

dfs()