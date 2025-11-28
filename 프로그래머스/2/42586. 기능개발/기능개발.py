from collections import deque

def solution(progresses, speeds):
    
    answer = []
    
    q = deque([(progress, i) for i, progress in enumerate(progresses)])
    
    while q:
        
        current_progress = []

        for j in range(len(q)):
            p, i = q.popleft()
            p += speeds[i]
            q.append((p, i))
            current_progress.append(p)

        cnt = 0
        for p in current_progress:
            if p < 100:
                break
            cnt += 1
        
        if cnt > 0:
            answer.append(cnt)
            for _ in range(cnt):
                q.popleft()
        
    return answer