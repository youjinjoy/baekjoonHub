import sys
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))

def solve():

    N = read_int()
    p1, p2 = read_list()
    
    M = read_int()

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = read_list()
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False for _ in range(N+1)]


    stack = [[p1,0]]
    visited[p1] = True

    answer = -1
    while stack:
        [cur, depth] = stack.pop()
        if cur == p2:
            answer = depth
            break

        for next in reversed(graph[cur]):
            if not visited[next]:                    
                stack.append([next, depth+1])
                visited[next] = True
    

    print(answer)

solve()
