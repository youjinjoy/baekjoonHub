import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

SA = sorted(set(A))

answer = []
cache ={}
for a in SA:
    cache[a] = bisect_left(SA, a)
for a in A:
    answer.append(cache[a])

print('\n'.join(map(str, answer)))