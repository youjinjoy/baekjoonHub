import sys
import math

input = sys.stdin.readline

a, b = list(map(int, input().rstrip().split(' ')))

prime_number = [True for _ in range(b + 1)]
prime_number[0] = prime_number[1] = False

for i in range(2, math.isqrt(b) + 1):

    if prime_number[i]:
        for j in range(i*i, b + 1, i):
            prime_number[j] = False

for k in range(a, b+1):
    if prime_number[k]:
        print(k)