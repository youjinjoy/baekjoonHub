import sys

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def solve():
    while True:
        try:
            ones = '1'
            digit = 1
            N = read_int()
            while int(ones) % N != 0:
                ones += '1'
                digit += 1
            print(digit)
        except:
            return
solve()