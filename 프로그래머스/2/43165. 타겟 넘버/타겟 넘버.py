def solution(numbers, target):
    global answer
    answer = 0
    backtrack([], numbers, target)
    
    return answer

def backtrack(result, numbers, target):
    global answer
    
    if len(result) == len(numbers):
        if calculate_with_op(numbers, result, target) == target:
            answer += 1
        return 0
    
    for op in ['+', '-']:
        result.append(op)
        backtrack(result, numbers, target)
        result.pop()

def calculate_with_op(numbers, ops, target):
    
    result = 0

    for i in range(len(numbers)):
        if ops[i] == '+' :
            result += numbers[i]
        else :  # op == '-'
            result -= numbers[i]
    
    return result