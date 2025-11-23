def solution(k, dungeons):
    
    visited = [False for _ in range(len(dungeons))]
    
    return backtrack(k, dungeons, visited)

def backtrack(remain, dungeons, visited):
    
    count = sum(visited)
    
    for i, (requirement, consumption) in enumerate(dungeons):

        if not visited[i] and remain >= requirement:

            visited[i] = True
            
            count = max(count, backtrack(remain - consumption, dungeons, visited))
            
            visited[i] = False
    
    return count