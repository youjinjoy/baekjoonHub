import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

SA = sorted(set(A))

for a in A:
    print(bisect_left(SA, a))