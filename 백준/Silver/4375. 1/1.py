import sys

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def solve():
    while True:
        try:
            digit = 1
            N = read_int()
            remainder = 1 % N
            while remainder != 0:
                remainder = (remainder * 10 + 1) % N
                digit += 1
            print(digit)
        except:
            return
        
solve()