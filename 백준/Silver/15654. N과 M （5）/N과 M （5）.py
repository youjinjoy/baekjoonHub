import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
arr.sort()
visited = [False for _ in range(N)]

result = []

def dfs():
    if len(result) == M:
        print(*result)
        return

    for i in range(0, N):
        if not visited[i]:
            visited[i] = True
            result.append(arr[i])
            dfs()
            visited[i] = False
            result.pop()

dfs()