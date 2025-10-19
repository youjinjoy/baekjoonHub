import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

SA = sorted(set(A))

cache = {a: i for i, a in enumerate(SA)}
answer = [cache[a] for a in A]

print(' '.join(map(str, answer)))