def solution(numbers, target):
    
    return dfs(0, 0, numbers, target)


def dfs(i, total, numbers, target):

    if i == len(numbers):
        return 1 if total == target else 0
    
    return dfs(i + 1, total + numbers[i], numbers, target) + dfs(i + 1, total - numbers[i], numbers, target) 