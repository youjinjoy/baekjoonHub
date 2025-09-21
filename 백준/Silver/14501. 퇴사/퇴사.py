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
    schedule = [read_list() for _ in range(N)]
    dp = [0 for _ in range(N+1)]

    for i, [T, P] in enumerate(reversed(schedule)):
        ri = N - i - 1
        if ri + T <= N:
            dp[ri] = max(dp[ri + 1], dp[ri + T] + P)
        else:
            dp[ri] = dp[ri + 1]

    print(max(dp))

solve()