import sys

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def solve():
    N = read_int() # N >= 1 
    steps = [read_int() for _ in range(N)]
    dp = [0 for _ in range(N)]

    dp[0] = steps[0]

    if N >= 2:
        dp[1] = steps[0] + steps[1]
    if N >= 3:
        dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2] + steps[i], dp[i-3] + steps[i-1] + steps[i])

    print(dp[N-1])
    
solve()