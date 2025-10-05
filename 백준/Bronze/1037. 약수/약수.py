import sys
from typing import List


def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    
    N  = read_int()
    divisors = read_list()
    divisors.sort()

    print(divisors[0] * divisors[-1])
    
solve()