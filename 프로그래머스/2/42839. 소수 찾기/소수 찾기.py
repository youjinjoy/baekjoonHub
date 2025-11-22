import math
from itertools import permutations

def solution(numbers):
    answer = 0
    
    n_list = list(numbers)
    p_list = set()
    # numbers로 만들 수 있는 조합
    ## itertools? dfs?
    for r in range(1, len(n_list) + 1):
        for p in permutations(n_list, r):
            p_list.add(int(''.join(map(str, p))))
            
    # 해당 조합의 숫자가 소수인지 판별
    # true로 판별된 개수 더하기
    for p in p_list:
        if is_prime(p):
            answer += 1

    return answer

def is_prime(number):
    
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    n = math.isqrt(number)
    
    for i in range(3, n + 1, 2):
        if number % i == 0:
            return False
    
    return True