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
    test_case = read_int()

    for _ in range(test_case):

        global D
        D = {}

        # input
        # -32768 ≤ x, y ≤ 32767
        global home, stores, j, dest
        s = read_int()

        home = read_list()
        D[0] = home

        stores = []
        j = 1
        for i in range(s):
            coor = read_list()
            stores.append(coor)
            D[i+1] = coor
            j = i+2

        dest = read_list()
        D[j] = dest

        global visited
        visited = [False for _ in range(j+1)]

        if bfs():
            print('happy')
        else:
            print('sad')

    return

def bfs():
    queue = deque([0])
    visited[0] = True
    
    while queue:
        current = queue.popleft()

        if D[current] == D[j]:
            return True
            
        for next in range(len(stores)+2):
            if not visited[next] and getDistance(D[current], D[next]) <= 1000:
                queue.append(next)
                visited[next] = True
    
    return False

def getDistance(first, second):
    dx = abs(first[0] - second[0])
    dy = abs(first[1] - second[1])
    return dx + dy


solve()