from collections import deque

def solution(queue1, queue2):
    # 두 큐의 모든 합 구하기 -> 한 큐 합이 그 절반에 해당하면 OK
    sum1, sum2 = sum(queue1), sum(queue2)
    total_sum = sum1 + sum2
    target_sum = total_sum // 2

    # 합이 홀수면 X
    if total_sum % 2 == 1:
        return -1
    
    # 큐 내 원소가 절반보다 크면 X
    for item1, item2 in zip(queue1, queue2):
        if item1 > target_sum or item2 > target_sum:
            return -1
        
    # 각 큐 합 추적
    QL = len(queue1)
    count1, count2 = 0, 0   # pop 한 횟수
    q1, q2 = deque(queue1), deque(queue2)
    while count1 < QL or count2 < QL:
    # 큰 수의 큐에서 팝해서 작은 수의 큐에 넣기를 반복
        if sum1 < sum2:
            N = q2.popleft()
            q1.append(N)
            count2 += 1
            sum1 += N
            sum2 -= N
        elif sum1 > sum2:
            N = q1.popleft()
            q2.append(N)
            count1 += 1
            sum1 -= N
            sum2 += N
        else:
            # 정답에 해당하면 카운트 반환
            return count1 + count2
            
    # 두 큐 전부 순회했으면 X
    return -1