import sys
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    n, k = read_list()
    coins = [read_int() for _ in range(n)]
             
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    for value in coins:
        for i in range(value, k + 1):
            dp[i] = dp[i] + dp[i - value if i - value >= 0 else 0]

    print(dp[k])
    
solve()