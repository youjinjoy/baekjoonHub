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

    for coin in coins:

        if coin > k:
            continue

        dp[coin] = 1

        for j in range(coin, k + 1):
            if dp[j-coin]:
                if dp[j]:
                    dp[j] = min(dp[j], dp[j-coin] + 1)
                else:
                    dp[j] = dp[j-coin] + 1

    print(dp[k] if dp[k] > 0 else -1)
    
    
solve()