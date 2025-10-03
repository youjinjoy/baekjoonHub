import sys

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def solve():
    N = read_int()
    
    dp = [0] * (N + 1)
    dp[0] = 1

    if N >= 2:
        dp[2] = 3
    
    for i in range(2, N + 1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i-j] * 2

    print(dp[N])
    
solve()