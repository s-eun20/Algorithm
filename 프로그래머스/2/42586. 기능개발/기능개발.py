from collections import deque
import math
def solution(progresses, speeds):
    days = deque()
    
    for p,s in zip(progresses,speeds):
        days.append(math.ceil((100 - p) / s))
        
    result = []
    
    while days :
        standard = days.popleft()
        count = 1
        
        while days and days[0] <= standard :
            days.popleft()
            count += 1
        
        result.append(count)
    
    
    return result