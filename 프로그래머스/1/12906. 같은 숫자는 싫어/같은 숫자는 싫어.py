def solution(arr):
    
    answer = []
    
    prev = -1
    for item in arr:
        if prev != item:
            answer.append(item)
        prev = item
    
    return answer