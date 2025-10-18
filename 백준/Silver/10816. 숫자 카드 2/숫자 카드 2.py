import sys
import bisect
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))
M = int(input())
X = list(map(int, input().split(' ')))

A.sort()

answer = []
for x in X:
    answer.append(bisect.bisect_right(A, x) - bisect.bisect_left(A,x))

print(' '.join(map(str, answer)))