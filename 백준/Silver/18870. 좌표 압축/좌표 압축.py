import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split(' ')))

SA = sorted(set(A))

def lower_bound(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

cache = defaultdict(lambda: None)
for a in A:
    if cache[a] is not None:
        print(cache[a])
    else:
        result = lower_bound(0, len(SA) - 1, SA, a)
        cache[a] = result
        print(result)