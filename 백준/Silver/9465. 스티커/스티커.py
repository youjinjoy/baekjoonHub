import sys
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))

def solve():
    tc = read_int()
    for _ in range(tc):
        c = read_int()  # c >= 1
        sticker = [read_list() for _ in range(2)]

        # 0: 위 뜯음. 1: 아래 뜯음
        dp = [[0 for _ in range(c)] for _ in range(2)]  # k 번째 열까지 최댓값
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]

        if c >= 2:
            dp[0][1] = sticker[1][0] + sticker[0][1]
            dp[1][1] = sticker[0][0] + sticker[1][1]
        for i in range(2, c):
            dp[0][i] = max(dp[0][i-2] + sticker[0][i], dp[1][i-2] + sticker[0][i], dp[1][i-1] + sticker[0][i])
            dp[1][i] = max(dp[1][i-2] + sticker[1][i], dp[0][i-2] + sticker[1][i], dp[0][i-1] + sticker[1][i])
        
        print(max(dp[0][-1],dp[1][-1]))
        
solve()