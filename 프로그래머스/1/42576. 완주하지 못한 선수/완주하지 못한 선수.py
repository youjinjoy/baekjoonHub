from collections import Counter

def solution(participant, completion):
    
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    
    remain = p_dict - c_dict

    return next(iter(remain))