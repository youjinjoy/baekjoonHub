def solution(word):
    answer = 0
    
    D = {}
    backtrack([], D, 0)
    
    return D[word]

def backtrack(result, D, cnt):
    word = ''.join(result)
    D[word] = cnt

    cnt += 1
    
    if len(result) == 5:
        return cnt
    
    for letter in ['A', 'E', 'I', 'O', 'U']:
        result.append(letter)
        cnt = backtrack(result, D, cnt)
        result.pop()
    
    return cnt
    
