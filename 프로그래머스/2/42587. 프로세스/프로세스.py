from collections import deque
def solution(priorities, location):
    queue = deque()
    
    #(원래 인덱스, 우선순위) 저장
    for i,priority in enumerate(priorities) :
        queue.append((i,priority))
        
    answer = 0
    
    while queue:
        index,priority = queue.popleft()
        
        flag = False
        
        for _, p in queue:
            if p > priority :
                flag = True
                break
                
        if flag :
            queue.append((index,priority))
            
        else :
            answer += 1
            
            if index == location :
                return answer
