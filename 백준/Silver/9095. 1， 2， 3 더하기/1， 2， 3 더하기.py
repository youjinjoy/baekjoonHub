import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

M = 0

numbers = [int(input()) for _ in range(tc)]
dp = [0 for _ in range(12)]
dp[1] = 1 # 1... 1
dp[2] = 2 # 1+1, 2 ... 2
dp[3] = 4 # 1+1+1, 1+2, 2+1, 3 ... 4
# 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 1+3, 3+1 ... 7

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for n in numbers:
    print(dp[n])