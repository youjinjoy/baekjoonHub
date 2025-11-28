import math

def solution(progresses, speeds):
    
    days = []
    
    for i, progress in enumerate(progresses):
        days.append(math.ceil((100 - progress) / speeds[i]))
    
    answer = []
    prev = days[0]
    cnt = 0
    for day in days:
        if day <= prev:
            cnt += 1
        else:
            answer.append(cnt)
            prev = day
            cnt = 1
    
    if cnt != 0:
        answer.append(cnt)

    return answer