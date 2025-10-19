import sys
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

cache = {}
start = 0
end = len(SA) - 1
for a in SA:
    cache[a] = lower_bound(start, end, SA, a)

for a in A:
    print(cache[a])