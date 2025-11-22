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
    
    prev = 0
    for i in range(k,N):
        if not visited[i] and prev != arr[i]:
            result.append(arr[i])
            visited[i] = True
            prev = arr[i]
            dfs(i+1)
            result.pop()
            visited[i] = False

dfs(0)