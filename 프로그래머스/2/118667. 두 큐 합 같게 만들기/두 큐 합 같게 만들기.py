from collections import deque
def solution(queue1, queue2):
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    # 두 큐의 합이 홀수면
    # 두 큐를 같게 만들 수 없음
    if (sum1+sum2) % 2 != 0 :
        return -1
    
    
    target = (sum1+sum2) // 2
    
    count = 0
    
    limit = (len(queue1)+len(queue2)) * 2
    
    while sum1 != sum2 :
        
        if count >= limit :
            return -1
        
        if sum1 > target :
            number = queue1.popleft()
            sum1 -= number
            queue2.append(number)
            sum2 += number
        else :
            number = queue2.popleft()
            sum2 -= number
            queue1.append(number)
            sum1 += number
            
        count += 1
        
        
    return count
    
    # 두 큐의 모든 합 계산
    # sum / 2 = 각 큐가 만들어야 할 합
    # 만약에 ~ 한 쪽 큐가 만들어야 할 합의 값 보다 크면 -> 반대 쪽으로 넘겨... 
    # 얼만큼 모자른지 계산 후에 그게 반대쪽에 있으면 꺼내온다?
    # 큐는 선입선출 ?
    