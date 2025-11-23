def solution(numbers, target):
    answer = [0]
    
    backtrack([], numbers, target, answer)
    
    return answer[0]

def backtrack(result, numbers, target, answer):
    
    if len(result) == len(numbers):
        if calculate_with_op(numbers, result, target) == target:
            answer[0] += 1
        return 0
    
    for op in ['+', '-']:
        result.append(op)
        backtrack(result, numbers, target, answer)
        result.pop()

def calculate_with_op(numbers, ops, target):
    
    result = 0

    for i in range(len(numbers)):
        if ops[i] == '+' :
            result += numbers[i]
        else :  # op == '-'
            result -= numbers[i]
    
    return result