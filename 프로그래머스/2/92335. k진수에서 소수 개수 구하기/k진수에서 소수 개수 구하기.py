import math

def solution(n, k):
    
    
    converted = convert_base(n, k)
    splitted = converted.split('0')
    
    count = 0
    
    for s in splitted:
        if not s: 
            continue
        
        if is_prime(int(s)):
            count += 1
            
    return count

def convert_base(n, k):
    
    digits='0123456789'
    result = ''
    
    while n > 0:
        n, r = divmod(n, k)        
        result = digits[r] + result        
    
    return result

def is_prime(n):
    if n == 0 or n == 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    m = math.isqrt(n)
    
    for i in range(3, m + 1):
        if n % i == 0:
            return False
        
    return True
