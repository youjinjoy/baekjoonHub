import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
result = []

def dfs(k):
    if len(result) == M:
        print(*result)
        return

    for i in range(k, N + 1):
        result.append(i)
        dfs(i)
        result.pop()

dfs(1)