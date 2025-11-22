import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
visited = [False for _ in range(N + 1)]
result = []

def dfs(k):
    if len(result) == M:
        print(*result)
        return

    for i in range(k, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)

            dfs(i + 1)

            visited[i] = False
            result.pop()

dfs(1)