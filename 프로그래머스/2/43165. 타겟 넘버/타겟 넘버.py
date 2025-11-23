def solution(numbers, target):
    
    return backtrack([], numbers, target)


def backtrack(result, numbers, target):
    answer = 0
    
    if len(result) == len(numbers):
        if calculate_with_op(numbers, result, target) == target:
            return 1
        return 0
    
    for op in ['+', '-']:
        result.append(op)
        answer += backtrack(result, numbers, target)
        result.pop()

    return answer
        
def calculate_with_op(numbers, ops, target):
    
    result = 0

    for i in range(len(numbers)):
        if ops[i] == '+' :
            result += numbers[i]
        else :  # op == '-'
            result -= numbers[i]
    
    return result