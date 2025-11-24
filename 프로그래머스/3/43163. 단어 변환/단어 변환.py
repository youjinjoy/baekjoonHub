def solution(begin, target, words):
    
    visited = [False for _ in range(len(words))]
    result = backtrack(begin, target, words, visited)
    return result if result < 50 else 0
    
def backtrack(cur, target, words, visited):

    cnt = 50
    
    if cur == target:
        return sum(visited)
    
    if sum(visited) == len(words):
        return 0
    
    for i in range(len(words)):
        if not visited[i] and is_convertable(cur, words[i]):
            visited[i] = True
            cnt = min(cnt, backtrack(words[i], target, words, visited))
            visited[i] = False

    return cnt

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