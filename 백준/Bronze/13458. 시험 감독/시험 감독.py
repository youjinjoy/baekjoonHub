import sys
from typing import List
import math

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    N = read_int()
    lectureRoom = read_list()
    P, A = read_list()

    answer = 0
    for candidates in lectureRoom:
        if candidates - P < 0:
            answer += 1
        else:
            answer += math.ceil((candidates - P) / A) + 1
    
    return answer

print(solve())