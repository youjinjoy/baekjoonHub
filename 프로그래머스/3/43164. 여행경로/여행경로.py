def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    visited = [False for _ in range(len(tickets))]

    result = dfs("ICN", visited, tickets, ["ICN"])
    return result

def dfs(end, visited, tickets, result):
    
    if len(result) == len(tickets) + 1:
        return True
    
    for i in range(len(tickets)):
        if not visited[i] and end == tickets[i][0]:
            visited[i] = True
            result.append(tickets[i][1])
            if dfs(tickets[i][1], visited, tickets, result):
                return result
            visited[i] = False
            result.pop()
    
    return False