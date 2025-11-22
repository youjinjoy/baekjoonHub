import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
arr.sort()
visited = [False for _ in range(N)]

result = []

def dfs(k):
    if len(result) == M:
        print(*result)
        return

    for i in range(k, N):
        result.append(arr[i])
        dfs(i + 1)
        result.pop()

dfs(0)