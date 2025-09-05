import sys
from collections import deque
# import heapq
# sys.setrecursionlimit(10**9)
# sys.stdin=open("test.txt")
input=sys.stdin.readline

n=int(input())
graph=[]
visited=[[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    line=list(map(int,input().strip()))
    graph.append(line)
# print(graph)
# print(visited)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    visited[a][b]=True
    house=1
    while queue:
        x,y=queue.popleft()
        # print(house,x,y)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and not visited[nx][ny]:
                # print(nx,ny)
                visited[nx][ny]=True
                house+=1
                queue.append((nx,ny))
    # print('-')
    # if house==0:
    #     house=1
    return house


danji=0
ans=[]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]==1:
            house=bfs(i,j)
            if house>0:
                danji+=1
                ans.append(house)
ans.sort()
print(danji)
# if not ans:
#     print(0)
# else:
#     for a in ans:
#         print(a)
for a in ans:
    print(a)
