import math

def solution(numbers):
    answer = 0
    
    n_list = list(numbers)
    p_list = set()
    # numbers로 만들 수 있는 조합
    ## itertools? dfs?
    p_list = get_candidates_from(numbers)
            
    # 해당 조합의 숫자가 소수인지 판별
    # true로 판별된 개수 더하기
    for p in p_list:
        if is_prime(p):
            answer += 1

    return answer

# 0 1 1
# 0 1 1
# 0 1 1

def get_candidates_from(numbers):

    candidates = set()
    
    def dfs(depth):
        if len(result) == depth:
            c = int(''.join(map(str,result)))
            candidates.add(c)
            return
        
        prev = -1
        for i in range(N):
            if not visited[i] and prev != numbers[i]:
                visited[i] = True
                result.append(numbers[i])
                prev = numbers[i]
                dfs(depth)
                visited[i] = False
                result.pop()

    N = len(numbers)
    
    for M in range(1, N + 1):
        visited = [False for _ in range(N)]
        result = []
        dfs(M)
    
    return list(candidates)

def is_prime(number):
    
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    n = math.isqrt(number)
    
    for i in range(3, n + 1, 2):
        if number % i == 0:
            return False
    
    return True