def solution(priorities, location):
    answer = 0
    
    runned = 0
    # max로 최댓값 찾기
    # 배열 순회하다가 찾으면 그 값 0으로 변경 및 runned += 1
    # location에 위치한 값이 0이 되면 return
    
    biggest = max(priorities)
    i = 0
    
    while True:

        if priorities[i] == biggest:
            runned += 1

            if i == location:
                return runned
            
            priorities[i] = 0
            biggest = max(priorities)
            
        # if runned == len(priorities):
        #     break

        i = (i+1) % len(priorities)
        
    
    # return runned