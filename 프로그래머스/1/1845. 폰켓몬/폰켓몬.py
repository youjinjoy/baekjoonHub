from collections import Counter

def solution(nums):
    answer = 0
    
    count = Counter(nums)
    N = len(nums)
    
    return N // 2 if len(count) >= N // 2 else len(count)
