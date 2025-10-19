import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

SA = sorted(set(A))

answer = []
for a in A:
    answer.append(bisect_left(SA, a))

print('\n'.join(map(str, answer)))