from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited=[0]*(n+1)

def bfs(v):
    global answer
    queue=deque()    
    queue.append(v)

    visited[v]=True
    answer=0
    
    while queue:
        v=queue.popleft()
    
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                answer+=1
    print(answer)

bfs(1)