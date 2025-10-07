def solution(msg):
    answer = []

    dict = {chr(i + 64): i for i in range(1,27)}
    num_index = 27
    
    p1, p2 = 0, 1
    last = 0
    while p1 < len(msg):
    ## 탐색
        ## 전체 문자열의 끝까지 갔으면 탈출
        if p2 >= len(msg):
            if dict.get(msg[p1:]):
                answer.append(dict[msg[p1:]])
            else:
                answer.append(last)
                answer.append(dict[msg[p2-1:]])
            break
            
        if dict.get(msg[p1:p2]):
        ## 해당 문자열이 있으면
            ## 진행
            last = dict.get(msg[p1:p2])
            p2 += 1
        else:
        ## 해당 문자열이 없으면
            ## 해당 문자열 등록
            dict[msg[p1:p2]] = num_index
            num_index += 1
            ## 최근 문자까지 해당하는 숫자 추가
            answer.append(last)
            ## 최근 문자부터 다시 진행
            p1 = p2 - 1
            
    return answer