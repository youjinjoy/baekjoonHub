from itertools import product
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []

    # Info Processing
    conditions = defaultdict(list)
    for data in info:
        lang, job, exp, food, score = data.split(' ')
        keys = [' '.join(p) for p in product((lang, '-'), (job, '-'), (exp, '-'), (food, '-'))]   
        for key in keys:
            conditions[key].append(int(score))
    
    for key in conditions.keys():
        conditions[key].sort()

    # Query Processing
    for q in query:
        lang, job, exp, food, score  = q.replace(' and ', ' ').split(' ')
        key = ' '.join([lang, job, exp, food])

        index = bisect.bisect_left(conditions[key], int(score))
        answer.append(len(conditions[key]) - index)
        
    return answer

def binary_search(arr, target): # lower bound
    start = 0
    end = len(arr)
    
    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1

    return start

