import sys
import heapq
# sys.setrecursionlimit(10**9)
# sys.stdin=open("test.txt")
input=sys.stdin.readline

n=int(input()) # 도시의 개수
m=int(input()) # 버스의 개수

graph=[[] for _ in range(n+1)]
# visited=[False]*(n+1)

dedup=[[100001 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a,b,cost=map(int,input().split())
    if cost<dedup[a][b]:
        graph[a].append((b,cost))   
# print(graph)

start,end=map(int,input().split())

answer=[float("inf")]*(n+1)
def bfs(start):
    hq=[]
    answer[start]=0
    d=answer[start]
    heapq.heappush(hq,(d,start))
    while hq:
        v=heapq.heappop(hq)
        dist=v[0] # 비용
        dest=v[1] # 목적지
        for nxt in graph[dest]:
            if dist+nxt[1]<answer[nxt[0]]:
                # nxt[0] 목적지
                # nxt[1] 비용
                answer[nxt[0]]=dist+nxt[1]
                heapq.heappush(hq,(dist+nxt[1],nxt[0]))
        if dest==end:
            break

bfs(start)
print(answer[end])