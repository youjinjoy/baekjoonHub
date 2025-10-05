import sys
from typing import List
import heapq as hq
from collections import deque
import math

input = sys.stdin.readline

a, b = list(map(int, input().rstrip().split(' ')))

for n in range(a, b + 1):
    
    if n == 1:
        continue
    
    if n == 2:
        print(n)
        continue
    
    if n % 2 == 0:
        continue
    
    m = math.isqrt(n)
    is_prime_number = True
    for i in range(3, m + 1, 2):
        if n % i == 0:
            is_prime_number = False
            break

    if is_prime_number:
        print(n)