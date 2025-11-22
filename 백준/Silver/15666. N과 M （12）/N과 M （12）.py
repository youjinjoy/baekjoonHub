import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

s = set(map(int, input().split(' ')))
a = sorted(list(set(s)))

result = []

def dfs(k):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(k, len(a)):
        result.append(a[i])
        dfs(i)
        result.pop()

dfs(0)