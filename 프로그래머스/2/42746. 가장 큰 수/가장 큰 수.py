from functools import cmp_to_key

def solution(numbers):
    
    def compare(a, b):
        if a + b < b + a:
            return 1
        elif a + b > b + a:
            return -1
        return 0
    
    numbers = list(map(str, numbers))
    numbers.sort(key = cmp_to_key(compare))
    
    
    return '0' if numbers[0] == '0' else ''.join(numbers)