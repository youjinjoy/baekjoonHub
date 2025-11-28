def solution(s):
    answer = True
    # 스택 2개 준비
    # 하나는 ) 저장
    # ) 저장된 스택이 비어있지만, 다른 스택에서 (가 꺼내지면 Fail
    
    s1 = list(s)
    s2 = []
    
    while s1:
        c = s1.pop()

        if c == ')':
            s2.append(c)
        else: # c == '('
            if len(s2) == 0:
                return False
            s2.pop()
    
    if len(s2) != 0:
        return False
        
    return True