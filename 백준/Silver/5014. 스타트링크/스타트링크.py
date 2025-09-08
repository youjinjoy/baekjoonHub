import sys
from typing import List
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))

def solve():

    max_floor, cur, dest, up, down = read_list()

    visited = [False for _ in range(0, max_floor+1)]

    queue = deque([[cur, 0]])
    visited[cur] = True

    while queue:
        floor, count = queue.popleft()
        
        if floor == dest:
            return count

        for next in [floor+up, floor-down]:
            
            if next <= 0 or next > max_floor:
                continue
            
            if visited[next]:
                continue

            if next == dest:
                return count+1

            queue.append([next, count+1])
            visited[next] = True
    
    return 'use the stairs'

print(solve())
