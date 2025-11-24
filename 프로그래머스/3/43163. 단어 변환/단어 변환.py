from collections import deque

def solution(begin, target, words):
    
    visited = set()
    queue = deque([(begin, 0)])
    
    while queue:
        cur, cnt = queue.popleft()
        
        if cur == target:
            return cnt
        
        for i in range(len(words)):
            if words[i] not in visited and is_convertable(cur, words[i]):
                visited.add(words[i])
                queue.append((words[i], cnt + 1))

    return 0
    
    visited = [False for _ in range(len(words))]
    
    

def is_convertable(word_a, word_b):
    n = len(word_a)
    
    count = 0
    
    for i in range(n):
        
        if word_a[i] != word_b[i]:
            count += 1
            
        if count >= 2:
            return False
    
    if count == 0:
        return False
    
    return True