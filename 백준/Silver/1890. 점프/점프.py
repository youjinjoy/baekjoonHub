import sys
# sys.setrecursionlimit(10**9)
# sys.stdin=open("test.txt")
n=int(input())

board=[]
for _ in range(n):
    line=list(map(int,input().split()))
    board.append(line)

dp=[[0 for _ in range(n)] for _ in range(n)]
# print(dp)
dp[0][0]=1

for i in range(n):
    for j in range(n):

        jump=board[i][j]

        if dp[i][j]!=0 and jump!=0:
            # 오른쪽 방향
            if i+jump<n:
                dp[i+jump][j]+=dp[i][j]
                # print('오른쪽에서 옴:', i,j, dp)

            # 아래쪽 방향
            if j+jump<n:
                dp[i][j+jump]+=dp[i][j]
                # print('왼쪽에서 옴:', i,j,dp)
        else:
            pass
print(dp[n-1][n-1])