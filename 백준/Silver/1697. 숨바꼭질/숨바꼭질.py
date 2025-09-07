import sys
from typing import List
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def read_list() -> List[int]:
    return list(map(int, input().split()))

def solve():

    N, K = read_list()

    if N >= K:
        return N-K

    visited = set()
    queue = deque([[N, 0]])
    visited.add(N)

    while queue:
        [cur, time] = queue.popleft()

        for next in [cur*2, cur+1, cur-1]:

            if next < 0 or next > 100000 or next in visited:
                continue

            if next == K:
                return time+1

            queue.append([next, time+1])
            visited.add(next)

            
print(solve())
