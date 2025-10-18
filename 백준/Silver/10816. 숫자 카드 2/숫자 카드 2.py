import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))
M = int(input())
X = list(map(int, input().split(' ')))

answer = []
C = Counter(A)
for x in X:
    answer.append(C[x])

print(' '.join(map(str, answer)))