import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))
arr.sort()

result = []

def dfs(k):
    if len(result) == M:
        print(*result)
        return

    for i in range(k, N):
        result.append(arr[i])
        dfs(i)
        result.pop()

dfs(0)