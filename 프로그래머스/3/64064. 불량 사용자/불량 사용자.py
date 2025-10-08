def solution(user_id, banned_id):
    # ["fr*d*", "*rodo", "******", "******"]
    # ["fr*d*", "*rodo", "******", "******"]
    # ["fr*d*", "*rodo", "******", "******"]
    # ["fr*d*", "*rodo", "******", "******"]
    answer_set = set()
    
    def dfs(index, path):
        
        if index == len(banned_id):
            answer_set.add(tuple(sorted(path)))
            return
        
        for u in user_id:
            if not u in path and match(u, banned_id[index]):
                
                path.append(u)
                dfs(index + 1, path)
                path.pop()

    dfs(0, [])
    answer = len(answer_set)

    return answer

def match(u, b):
    if len(u) != len(b):
        return False
    
    for i in range(len(u)):
        if b[i] != '*' and u[i] != b[i]:
            return False
    
    return True