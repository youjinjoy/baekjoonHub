def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    stack = []
    for i, price in enumerate(prices):
        
        while stack and stack[-1][0] > price:
            cp, ci = stack.pop()
            answer[ci] = i - ci
        
        stack.append((price, i))
        
    
    while stack:
        cp, ci = stack.pop()
        answer[ci] = len(prices) - 1 - ci

    
    return answer