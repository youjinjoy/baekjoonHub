import sys
import bisect
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split(' ')))

M = int(input())
targets = list(map(int, input().split(' ')))

numbers.sort()
for target in targets:
    idx = bisect.bisect_left(numbers, target)
    if idx < N and numbers[idx] == target:
        print(1)
    else:
        print(0)