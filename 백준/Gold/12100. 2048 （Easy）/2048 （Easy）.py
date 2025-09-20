import sys
from typing import List

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_list() -> List[int]:
    return list(map(int, input().split()))


def solve():
    N = read_int()
    board = [read_list() for _ in range(N)]

    global answer
    answer = 0

    for i in range(4):
        dfs(board, N, i, 0)
    
    return answer

def dfs(board, N, d, depth):
    global answer

    if depth >= 5:
        answer = max(answer,max(max(row) for row in board))
        return
    
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    if d == 0:
        # 왼쪽
        for i in range(N):
            merged_row = get_merged_line(board[i])
            for j in range(N):
                new_board[i][j] = merged_row[j]
    
    elif d == 1:
        # 오른쪽
        for i in range(N):
            reversed_row = list(reversed(board[i]))
            merged_reversed_row = get_merged_line(reversed_row)
            for j in range(N):
                new_board[i][j] = merged_reversed_row[N-j-1]

    elif d == 2:
        # 위쪽
        for i in range(N):
            column = []
            for j in range(N):
                column.append(board[j][i])
            merged_column = get_merged_line(column)
            for j in range(N):
                new_board[j][i] = merged_column[j]

    elif d == 3:
        # 아래쪽
        for i in range(N):
            column = []
            for j in range(N):
                column.append(board[j][i])
            reversed_column = list(reversed(column))
            merged_reversed_column = get_merged_line(reversed_column)
            for j in range(N):
                new_board[j][i] = merged_reversed_column[N-j-1]

    for i in range(4):
        dfs(new_board, N, i, depth + 1)

def get_merged_line(line):
    i = 0
    result = []
    last = 0

    while i < len(line):
        if line[i] == 0:
            pass
        elif last == 0 and line[i] > 0:
            last = line[i]
        elif line[i] == last:
            result.append(last*2)
            last = 0
        else:
            result.append(last)
            last = line[i]
        i += 1
    
    if last != 0:
        result.append(last)
    
    while len(result) < len(line):
        result.append(0)
    
    return result
        


print(solve())